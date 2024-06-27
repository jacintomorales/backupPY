# Herramienta para enviar mensaje a BOT de telegram con archivo adjunto
# --version 2.0
# Prerequisitos: 
# S.O: Linux
# -- python 3.6 o superior
# -- apt-get install python3-python-telegram-bot
# Autor: https://github.com/jacintomorales
# Ejemplo: python3 telegram.py -t <TOKENAPI> -c <CHATID> -m <MESSAGE> -f <FILE> 

import argparse
import os

from telegram import Bot
from telegram.utils.request import Request
from telegram.error import TelegramError

### Funciones ###

def sendTelegram(token, chatid, message=None, file=None):

    try:
        request = Request(con_pool_size=8)
        bot = Bot(token=token, request=request)

        if file:
            if os.path.exists(file):
                with open(file, 'rb') as f:
                    bot.send_document(chat_id=chatid, document=f, caption=message)
            else:
                print("El archivo " + file + " no existe")
        else:
            if token and chatid:
                bot.send_message(chat_id=chatid, text=message)
                print("Enviando mensaje por telegram al chat: " + str(chatid))
            else:
                print("Recuerda el TOKEN y el CHATID")

        print("Mensaje enviado por telegram al chat:" + str(chatid))

    except TelegramError as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Envío de mensajes y archivos a bot de Telegram")
    parser.add_argument('-t', '--token', type=str, help='Token API del bot de Telegram', required=True)
    parser.add_argument('-c', '--chatid', type=int, help='ID del chat de Telegram', required=True)
    parser.add_argument('-m', '--message', type=str, help='Mensaje a enviar a través de Telegram')
    parser.add_argument('-f', '--file', type=str, help='Ruta del archivo a enviar')

    args = parser.parse_args()
    sendTelegram(args.token, args.chatid, args.message, args.file)