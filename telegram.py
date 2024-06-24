import argparse
import requests

parser = argparse.ArgumentParser(description="Envio de mensajes a bot de telegram")
parser.add_argument('-t', '--token', type=str, help='TokenAPI del bot de telegram', required=True)
parser.add_argument('-c', '--chatid', type=int, help='ID del chat de telegram', required=True)
parser.add_argument('-m', '--message', type=str, help='Mensaje a enviar a traves de telegram')

args = parser.parse_args()

try:
        url="https://api.telegram.org/bot"
        method="sendMessage"

        if args.token and args.chatid:
                data={'chat_id': args.chatid, 'text': args.message}
                r = requests.post(url+args.token+"/"+method, data).json()
                print(r)
        else:
                print("Recuerda el TOKEN y el CHATID")

except requests.exceptions.HTTPError as e:
        print(e)