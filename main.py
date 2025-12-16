main.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

TOKEN = "7966362624:AAGDG_tDDOujCoyBhp_E5HunvbQHk6b8kDQ"
GROUP_LINK = "https://t.me/+UhZo8ZsUECYyYWI1"

def start(update, context):
    msg = (
            "🌸 Hiiiii~ 🌸\n\n"
                    "Main Trishu hoon 🤍\n"
                            "Adarsh ki cute si Nezuko-style chatting bot 🥰\n\n"
                                    "Main Hinglish me baat karti hoon 😌\n\n"
                                            "✨ Hamare group me join karo ✨\n"
                                                    f"{GROUP_LINK}"
                                                        )
                                                            update.message.reply_text(msg)

                                                            def chat(update, context):
                                                                replies = [
                                                                        "Hehe 😄",
                                                                                "Awww 🥺 tum sweet ho",
                                                                                        "Nezuko mode ON 🔥",
                                                                                                "Owner Adarsh best hain 😌",
                                                                                                        "Haha 😂"
                                                                                                            ]
                                                                                                                update.message.reply_text(random.choice(replies))

                                                                                                                updater = Updater(TOKEN, use_context=True)
                                                                                                                dp = updater.dispatcher

                                                                                                                dp.add_handler(CommandHandler("start", start))
                                                                                                                dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

                                                                                                                updater.start_polling()
                                                                                                                updater.idle()

