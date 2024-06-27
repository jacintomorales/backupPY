# backupPY

backupPY es un conjunto de scripts en Python diseñados para realizar copias de seguridad completas e incrementales con un registro detallado en texto plano, utilizando la herramienta de compresión TAR, disponible en sistemas operativos UNIX/Linux.

### ¿Por qué usar backupPY?

Como Director de IT en varias empresas, he utilizado la herramienta TAR para crear copias de seguridad de archivos y directorios con información crítica. Aunque TAR es potente para automatizar este proceso, siempre quedaba con la duda de si la copia se había realizado correctamente. Esto me obligaba a verificar manualmente los directorios y su contenido, un proceso que consumía mucho tiempo debido al gran número de copias de seguridad que debía gestionar. Por ello, decidí crear esta herramienta, que además de realizar copias de seguridad convencionales, incluye las siguientes mejoras:

### Mejoras

1. **Generación automática de nombres de archivo:**
   - El nombre del archivo se genera automáticamente con la fecha y hora actual en el formato `RUTA/YMD-HHMMSS.tar.gz` para copias normales, `RUTA/YMD-HHMMSS_full.tar.gz` para copias completas, o `RUTA/YMD-HHMMSS_inc.tar.gz` para copias incrementales.

2. **Archivo de registro:**
   - Se generan dos archivos principales al realizar una copia: el archivo comprimido (`*.tar.gz`) y un archivo de registro detallado (`*.tar.gz.log`) que contiene los nombres de los archivos y directorios respaldados.

3. **Copia completa:**
   - Con la opción `-f` o `--full`, además de los dos archivos anteriores, se crea el archivo `full.snapshot` para las copias incrementales posteriores.

4. **Copia incremental:**
   - Con la opción `-i` o `--incremental`, solo se copian los archivos creados después de la última copia completa. No es necesario especificar el archivo de snapshot; el script buscará `full.snapshot` en el directorio de destino. Nota: Debes crear una copia completa previamente.

5. **Exclusiones simplificadas:**
   - Con la opción `-e` o `--exclude`, puedes excluir directorios o archivos de la copia de seguridad de manera simplificada: `-e RUTA1 RUTA2 RUTA3`.

6. **Notificaciones a Telegram:**
   - Con la opción `-t` o `--telegram TOKENAPI CHATID`, se enviará una notificación a través de Telegram con la siguiente información:
     - Archivo de registro (`*.tar.gz.log`)
     - Nombre del archivo de la copia de seguridad
     - Fecha de ejecución
     - Tamaño del archivo en Megabytes (MB)
   - **Nota importante:** Debes crear un BOT y un CHAT para el Bot en Telegram. Aquí te dejo los pasos para hacerlo.

Próximamente, añadiré la notificación por correo electrónico.

## Modo de uso

### Requisitos
- Sistema Operativo: Unix / Linux
- Python 3 o posterior
  ```bash
  sudo apt-get install python3
  python3 --version
- Libreria oficina de TELEGRAM-BOT
```
sudo apt-get install python3-python-telegram-bot
```
o 
```
pip install python-telegram-bot
```

## Instalacion backupPY

Existen 2 formas de poder utilizar esta herramienta. 

1) Sitio de GITHUB
- Visita la página principal del repositorio en GitHub.
- Haz clic en el botón verde "Code" cerca de la esquina superior derecha.
- Selecciona "Download ZIP" para descargar el repositorio como un archivo comprimido ZIP.
- Descomprime el archivo ZIP descargado en tu computadora. Obtendrás una carpeta con el nombre del repositorio que contiene todos los archivos del proyecto.

2) Clona el repositorio de GITHUB (Debes tener GIT instalado)
```
bash
cd /opt
git clone https://github.com/jacintomorales/backupPY.git
```

Una vez realizada la instalacion backupPY, busca en internet un manual para crear el bot de telegram con BootFather y obten el TOKEN y el CHATID necesario.

## Manual de usuario:

1) Sintaxis: 

```
python3 backup.py -s ORIGEN -d DESTINO -e EXCLUDE1 EXCLUDE2 EXCLUDE3 --full -t TOKENAPI CHATID
```

2) Opciones: 

- -s o --source se acompaña con el directorio de origen de la copia
- -d o --destination se acompaña con el directorio de destino
- -e o --exclude. Acompañalo con multiples directorios dpara excluir
- -f o --full. Indica que el backup es completo
- -i o --incremental. Indica que el backup es incremental
- -t o --telegram. acompañado con el TOKENAPI del Bot y el CHATID te enviara la notificacion a telegram. 


