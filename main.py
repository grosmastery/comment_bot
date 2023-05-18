from pyrogram import Client, filters
import random
import time

# в файл config.ini потрібно вписати api_id, api_hash, та дані для проксі.
app = Client("account")

key_words = {"test", "test2", "test3"}


def reply_to_message(message):
    reply_text = "test text"

    message.reply(reply_text, quote=True)
    time.sleep(random.randint(5, 60))


@app.on_message(filters.text | filters.photo)
def parse(client, message):
    if any(word in (message.text or '') or word in (message.caption or '') for word in key_words):
        reply_to_message(message)


app.run()
