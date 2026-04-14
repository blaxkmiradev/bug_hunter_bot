# bot.py
import telebot
from dorks import DORK_TEMPLATES

# ==========================================
# IMPORTANT: Replace this with your actual Bot Token from @BotFather
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
# ==========================================

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Handles the /start and /help commands."""
    welcome_text = (
        "Welcome to the **Bug Hunter Dork Bot**! 🕵️‍♂️\n\n"
        "Send me a target domain (e.g., `example.com` or `tesla.com`), "
        "and I will generate a list of Google Dorks for your recon phase."
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def generate_dorks(message):
    """Handles all other text messages (assuming they are domains)."""
    domain = message.text.strip().lower()
    
    # Basic check to ensure the user didn't send a long paragraph
    if " " in domain and not domain.startswith('"'):
        bot.reply_to(message, "⚠️ Please send a valid domain name or keyword (e.g., `example.com`).")
        return

    # Let the user know the bot is working
    bot.send_chat_action(message.chat.id, 'typing')
    
    response_msg = f"🔍 **Generated Dorks for target:** `{domain}`\n\n"
    
    # Generate the dorks by formatting the templates from dorks.py
    for category, template in DORK_TEMPLATES.items():
        # Replace the {domain} placeholder with the user's input
        dork = template.format(domain=domain)
        # Format as monospaced code blocks for easy copying in Telegram
        response_msg += f"*{category}:*\n`{dork}`\n\n"
    
    response_msg += "🛡️ *Happy Hunting! Remember to only test targets you have explicit permission to test.*"
    
    # Send the final message
    try:
        bot.reply_to(message, response_msg, parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, "An error occurred while generating the message. Please try again.")
        print(f"Error: {e}")

if __name__ == '__main__':
    print("🤖 Bot is starting up...")
    print("Press Ctrl+C to stop.")
    # none_stop=True ensures the bot keeps polling even if an error occurs
    bot.polling(none_stop=True)
