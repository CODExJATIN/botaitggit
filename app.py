import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Initialize the OpenAI API with your credentials
openai.api_key = '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'

# Define a function to generate a response using ChatGPT
def generate_response(text):
    prompt = f"Q: {text}\nA:"
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define a function to handle incoming messages from users
def handle_message(update, context):
    text = update.message.text
    response = generate_response(text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Set up the Telegram bot
updater = Updater(token='6138109313:AAGYd8Ab4dEyycP1JDwcmCY5F8EWLK5euIw', use_context=True)
dispatcher = updater.dispatcher

# Set up a message handler to call the handle_message function
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
