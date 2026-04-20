#!/usr/bin/env python3
"""
Telegram File Uploader Bot
A safe and legitimate bot for handling user files via Telegram.
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        "👋 Welcome! I am a safe file uploader bot.\n\n"
        "Send me any file (document, photo, etc.) and I will send it back to you.\n"
        "This bot demonstrates safe file handling practices."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "📚 *Help Guide*\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n\n"
        "Simply send me any file and I'll process it safely!"
    )

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming files (documents, photos, etc.)."""
    file = None
    file_type = "unknown"
    
    # Determine file type and get file object
    if update.message.document:
        file = update.message.document
        file_type = "document"
    elif update.message.photo:
        # Get the largest photo
        file = update.message.photo[-1]
        file_type = "photo"
    elif update.message.audio:
        file = update.message.audio
        file_type = "audio"
    elif update.message.voice:
        file = update.message.voice
        file_type = "voice"
    elif update.message.video:
        file = update.message.video
        file_type = "video"
    
    if not file:
        return
    
    try:
        # Send acknowledgment
        await update.message.reply_text(f"📥 Received {file_type}. Processing safely...")
        
        # Get the file from Telegram
        telegram_file = await context.bot.get_file(file.file_id)
        
        # Create a temporary filename
        temp_filename = f"temp_{file.file_unique_id}"
        if hasattr(file, 'file_name') and file.file_name:
            temp_filename = f"temp_{file.file_unique_id}_{file.file_name}"
        
        # Download file temporarily
        local_path = await telegram_file.download_to_drive(temp_filename)
        
        logger.info(f"Downloaded {file_type} to {local_path}")
        
        # Send the file back to demonstrate safe handling
        if file_type == "photo":
            await update.message.reply_photo(photo=open(local_path, 'rb'))
        elif file_type == "document":
            await update.message.reply_document(document=open(local_path, 'rb'))
        elif file_type == "audio":
            await update.message.reply_audio(audio=open(local_path, 'rb'))
        elif file_type == "voice":
            await update.message.reply_voice(voice=open(local_path, 'rb'))
        elif file_type == "video":
            await update.message.reply_video(video=open(local_path, 'rb'))
        
        await update.message.reply_text("✅ File processed and sent back successfully!")
        
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        await update.message.reply_text(f"❌ Error processing file: {str(e)}")
    
    finally:
        # Clean up temporary file
        try:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
                logger.info(f"Cleaned up temporary file: {temp_filename}")
        except Exception as e:
            logger.error(f"Error cleaning up file: {e}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors caused by updates."""
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    """Start the bot."""
    # Get token from environment variable
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set!")
        return
    
    # Create the Application
    application = Application.builder().token(token).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Handle various file types
    application.add_handler(MessageHandler(
        filters.Document.ALL | filters.PHOTO | filters.AUDIO | filters.VOICE | filters.VIDEO,
        handle_file
    ))
    
    # Log errors
    application.add_error_handler(error_handler)
    
    # Start the Bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
