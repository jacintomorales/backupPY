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

### Argumentos parser ###

parser = argparse.ArgumentParser(description='Copia de seguridad de archivos y directorios con TAR')
parser.add_argument('-s', '--source', help='ruta de origen de las carpetas a copiar', required=True)
parser.add_argument('-d', '--destination', help='ruta de destino donde se guardara la copia de seguridad', required=True)
parser.add_argument('-e', '--exclude', type=str, nargs='*', default=None, help='ruta de carpetas que no quieres que esten en la copia')
parser.add_argument('-r', '--register', type=str, default=None, help='archivo donde se guardara la salida de la copia de seguridad', required=False)
parser.add_argument('-f', '--full', action='store_true', help='se indica que el backup es completo')
parser.add_argument('-i', '--incremental', action='store_true', help='se indica que el backup es diferencial')

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
						#pathsExclude=removeEndSwith(exclude)
					else: 
						print("el directorio " + exclude + " no existe. No se tendra en cuenta")
				excludeStr=' '.join(excludeList)
				
				if args.full:
					snapshot=destination + "/full.snapshot"
					if os.path.exists(snapshot):
						print("eliminando SNAPSHOT existente en " + snapshot)
						subprocess.check_output("rm " + snapshot, shell=True, stderr=subprocess.STDOUT, text=True)
						print("creado nuevo SNAPSHOT .... ")
						subprocess.check_output("touch " + snapshot, shell=True, stderr=subprocess.STDOUT, text=True)
					else:
						print("creado nuevo SNAPSHOT .... ")
						subprocess.check_output("touch " + snapshot, shell=True, stderr=subprocess.STDOUT, text=True)

					command="tar -cvzg " + snapshot + " -f " + destination + "/" + _datetime + "_full.tar.gz " + excludeStr + ' ' + source
				elif args.incremental:
					snapshot=destination + "/full.snapshot"
					if os.path.exists(snapshot):
						command="tar -cvzg " + snapshot + " -f " + destination + "/" + _datetime + "_inc.tar.gz " + excludeStr + ' ' + source
					else:
						print("el archivo de SNAPSHOT no existe, debes realizar un backup completo con anterioridad")
				else:
					command="tar -cvzf " + destination + "/" + _datetime + ".tar.gz " + excludeStr + ' ' + source
		else:
				command="tar -cvzf " + destination + "/" + _datetime + ".tar.gz " + source

		print("ejecutando la copia de seguridad ...")
		result=subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
		print("La copia se ha guardado como " + _datetime + ".tar.gz en el directorio " + destination)
		
	else:
		if not os.path.exists(args.source) and not os.path.exists(args.destination):
			print("No existe los directorios " + args.source + " y " + args.destination)
		elif not os.path.exists(args.source):
			print("no existe el directorio " + args.source)
		elif not os.path.exists(args.destination):
			print("no existe el directorio " + args.destination)
		
except subprocess.CalledProcessError as e:
	print(e)
