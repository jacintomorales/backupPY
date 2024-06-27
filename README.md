# backupPY 

Es un conjunto de Scripts en python para hacer copias de seguridad completas e incrementales con un registro detallado en texto plano utilizando la herramienta de compresion TAR que existe en sistemas operativos UNIX/Linux.

### El por que ? 

Como parte de mi experiencia como Director de IT en alguna empresas he utilizado la herramienta TAR esencialmente a la hora de crear copias de seguridad de los archivos y directorios que tienen informacion critica para estas compañias y aunque con esta potente herramienta podia crear mis tareas programadas y automatizar un poco este proceso, siempre quedaba con la duda si si se habia hecho bien la copia. Asi que entraba al servidor, y comenzaba a buscar los directorios uno a uno, miraba si estos tenian el tamaño correcto y si su contenido era el correcto. Trabajo que me quitaba mucho tiempo ya que eran mas de 10 copias de seguridad de distintos servicios. Por tal motivo, decidi crear esta herramienta, que adicional a la copia de archivos convencional tiene los siguientes caracteristicas adicionales. 

### Mejoras

1) Ya no es necesario que especifiques el nombre del archivo. Este lo va a crear automaticamente con la fecha y tiempo actual en formato de salida para el nombre del archivo RUTA/YMD-HHMMSS.tar.gz si es una copia normal o RUTA/YMD-HHMMSS_full.tar.gz si es completa o RUTA/YMD-HHMMSS_inc.tar.gz si es incremental.

2) Archivo de registro de copias: se genera principalmente 2 archivos al momento de la copia. el primero sera el archivo comprimido terminada en *.tar.gz y el segundo un archivo de registro detallado que contiene los nombres de archivos y directorios que fueron respaldados con nombre *.tar.gz.log

3) Si especificas la opcion -f o la opcion --full, aparte de que te crea los 2 archivos anteriores, de va a crear el archivo full.snapshot que utilizaremos para las copias incrementales posteriores. 

4) Si especificas la opcion -i o --incremental, este solo hara copia de los archivos que fueron creados en fechas posteriores a la ultima copia completa. No va a ser necesario que especifiques el archivo de snapshot, el va a tomar el directorio de destino y lo va a buscar como full.snapshot. NOTA: Debes crear con anterioridad una copia completa. 

5) Se simplifica la forma de agregar exlusiones: con la opcion -e o --exclude vas a poder ingresar los directorios o archivos que quieras excluir de la copia de la siguiente manera "-e RUTA1 RUTA2 RUTA3 RUTA4" ... Se creo para minimizar el procesos de agregar por cada archivo o directorio el "--exclude=" que tiene como requisito la utilidad TAR.

6) Notificaciones a TELEGRAM: que mejor manera de mantenernos informados si se creo o no una copia que enviando los datos mas importantes con un mensaje a traves de telegram. Especificando la opcion -t o --telegram TOKENAPI CHATID enviara una notificacion con la siguiente informacion: 

- Archivo de registor *.tar.gz.log de la copia
- Nombre del archivo en donde se almaceno la copia de seguridad
- Fecha de ejecucion
- Tamaño del archivo en MegaBytes (MB)

NOTA IMPORTANTE: Es necesario que crees un BOT y un CHAT para el Bot dentro de telegram. Aca te dejo los pasos para hacerlo. 

Proximanente estare adicionando la notificacion por correo electronico.

# MODO DE USO

### Requisitos
- Sistema Operativos: Unix / Linux
- Python3 o posterior

```bash
sudo apt-get install python3
python3 --version```

- Libreria oficina de TELEGRAM-BOT

```sudo apt-get install python3-python-telegram-bot```
o 
```pip install python-telegram-bot```


