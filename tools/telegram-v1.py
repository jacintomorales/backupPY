# Herramienta para enviar mensaje a BOT de telegran
# --version 1.0
# Prerequisitos: 
# S.O: Linux
# -- python 3.5 o superior
# Autor: https://github.com/jacintomorales
# Ejemplo: python3 telegram.py -t <TOKENAPI> -c <CHATID> -m <MESSAGE> 

import argparse
import requests

### Funciones ###
def sendTelegram(token, chatid, message):
        try:
                url="https://api.telegram.org/bot"
                method="sendMessage"

                if token and chatid:
                        data={'chat_id': chatid, 'text': message}
                        r = requests.post(url+token+"/"+method, data).json()
                        print("Enviando mensaje a telegram al chat: " + chatid)
                else:
                        print("Recuerda el TOKEN y el CHATID")

        except requests.exceptions.HTTPError as e:
                print(e)

### Codigo ###

if __name__ == "__main__":

        parser = argparse.ArgumentParser(description="Envio de mensajes a bot de telegram")
        parser.add_argument('-t', '--token', type=str, help='TokenAPI del bot de telegram', required=True)
        parser.add_argument('-c', '--chatid', type=int, help='ID del chat de telegram', required=True)
        parser.add_argument('-m', '--message', type=str, help='Mensaje a enviar a traves de telegram')

        args = parser.parse_args()
        sendTelegram(args.token, args.chatid, args.message)