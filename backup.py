# Herramienta para crear copias de seguridad completas o incrementales. Adicional podras notificar
# el resultado de ejecucion de las mismas a traves de telegram o correo electrico con datos relevantes
# para su registro (fecha de ejecucion, tamaño y ubicacion)
# --version 1.0
# Prerequisitos: 
# S.O: Linux
# -- tar
# -- python3
# Autor: https://github.com/jacintomorales
# Ejemplo 1: python3 backup.py -s <FUENTE> -d <DESTINO> --exclude <RUTA1> <RUTA2> --full 
# Ejemplo 2: python3 backup.py -s <FUENTE> -d <DESTINO> ---exclude <RUTA1> <RUTA2> --incremental
# Ejemplo 3: python3 backup.py -s <FUENTE> -d <DESTINO> --exclude <RUTA1> <RUTA2>
# Ejemplo 4: python3 backup.py -s <FUENTE> -d <DESTINO>

import os
import subprocess
import argparse
from datetime import datetime
from telegram import sendTelegram

### Argumentos parser ###

parser = argparse.ArgumentParser(description='Copia de seguridad de archivos y directorios con TAR')
parser.add_argument('-s', '--source', help='ruta de origen de las carpetas a copiar', required=True)
parser.add_argument('-d', '--destination', help='ruta de destino donde se guardara la copia de seguridad', required=True)
parser.add_argument('-e', '--exclude', type=str, nargs='*', default=None, help='ruta de carpetas que no quieres que esten en la copia')
parser.add_argument('-f', '--full', action='store_true', help='se indica que el backup es completo')
parser.add_argument('-i', '--incremental', action='store_true', help='se indica que el backup es diferencial')
parser.add_argument('-t', '--telegram', type=str, nargs=2, default=None, help='se enviara un mensaje al bot de telegram. Se espera <TOKENAPI> <CHATID>', required=False)

args = parser.parse_args()

### Funciones ###

def removeEndSwith(path):
	newpath=""
	if path.endswith('/'):
		newpath=path[:-1]
	else:
		newpath=path
	return newpath

### Codigo ###

try:
	if os.path.exists(args.source) and os.path.exists(args.destination):
		source=removeEndSwith(args.source)
		destination=removeEndSwith(args.destination)
				
		now=datetime.now()
		_datetime = now.strftime("%Y%m%d-%H%M%S")

		if args.exclude is not None:
				excludeList=[]
				for exclude in args.exclude:
					if os.path.exists(exclude):
						pathExclude=removeEndSwith(exclude)
						excludeList.append("--exclude="+ pathExclude)

					else: 
						print("el directorio " + exclude + " no existe. No se tendra en cuenta")
				excludeStr=' '.join(excludeList)
				
				if args.full:
					snapshot=destination + "/full.snapshot"
					if os.path.exists(snapshot):
						print("eliminando SNAPSHOT existente en " + snapshot)
						subprocess.check_output("rm -f " + snapshot, shell=True, stderr=subprocess.STDOUT)
						print("creado nuevo SNAPSHOT .... ")
						subprocess.check_output("touch " + snapshot, shell=True, stderr=subprocess.STDOUT)
					else:
						print("creado nuevo SNAPSHOT .... ")
						subprocess.check_output("touch " + snapshot, shell=True, stderr=subprocess.STDOUT)
					filename=destination + "/" + _datetime + "_full.tar.gz"
					command="tar -cvzg " + snapshot + " -f " + filename + " " + excludeStr + ' ' + source

				elif args.incremental:
					snapshot=destination + "/full.snapshot"
					if os.path.exists(snapshot):
						filename=destination + "/" + _datetime + "_inc.tar.gz"
						command="tar -cvzg " + snapshot + " -f " + filename + " " + excludeStr + ' ' + source
					else:
						print("el archivo de SNAPSHOT no existe, debes realizar un backup completo con anterioridad")
				else:
					filename=destination + "/" + _datetime + ".tar.gz"	
					command="tar -cvzf " + filename + " " + excludeStr + ' ' + source
		else:
				filename=destination + "/" + _datetime + ".tar.gz"
				command="tar -cvzf " + filename + " " + source
				
		print("ejecutando la copia de seguridad ...")
		
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		stdout, _ = process.communicate()
		logFile=filename + ".log"

		with open(logFile, 'a') as log_file:
			log_file.write(stdout.decode('utf-8'))

		if args.telegram:
			tokenapi, chatid = args.telegram
			message=""
			if os.path.exists(filename):
				size=os.path.getsize(filename) / (1000 * 1000)
				message="🆗🆗🆗 BACKUP EXITOSO 🆗🆗🆗 ,📁 " + filename + " 📁, 📅 " + now.strftime("%Y-%M-%d") + " 📅, 🪨 " + str(size) + " MB"
			sendTelegram(tokenapi, chatid, message)

		print(filename)
		
	else:
		if not os.path.exists(args.source) and not os.path.exists(args.destination):
			print("No existe los directorios " + args.source + " y " + args.destination)
		elif not os.path.exists(args.source):
			print("no existe el directorio " + args.source)
		elif not os.path.exists(args.destination):
			print("no existe el directorio " + args.destination)
		
except subprocess.CalledProcessError as e:
	print(e)
