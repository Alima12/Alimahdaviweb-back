from rest_framework.views import APIView
import json
from telegram.ext import Dispatcher, MessageHandler, Filters
from telegram import Update, Bot
from django.http.response import JsonResponse

bot = Bot(token="5515102830:AAFSh_McX1ah0kdpBGDyM40qRmQZtHNEhnc")
dispatcher = Dispatcher(bot, None, use_context=True)


def echo(update, context):
    chat_id = update.message.chat_id
    chat_user = update.message.from_user
    chat_text = update.message.text

    context.bot.send_message(chat_id=chat_id, text="Message from " + str(chat_user.first_name) + ": \n " + chat_text)


def receive_messages(request, *args, **kwargs):
    # print(request)
    data = request.POST
    str_data = json.dumps(data)
    print(str_data)
    if request.method == "POST":
        dispatcher.add_handler(MessageHandler(Filters.text, echo))
        try:
            dispatcher.process_update(
                Update.de_json(data, bot)
            )

        except Exception as e:
            print(e)
            return {"statusCode": 500}

        return {"statusCode": 200}
    else:
        Bot.sendMessage(chat_id=1074680699, text=str_data)
        return JsonResponse({
            "status":500,
            "msg": "Get method was not allowed"
        })


