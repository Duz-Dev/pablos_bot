# Bot de discord "Pablo bot 🗣️"

Indicaciones.

- El bot fue hecho en python 3.12.2
- Necesitas tener creado tu "bot" de discord con antelación desde la plataforma de desabolladores de discord, ya que este repositorio solo es una base para programar dicho bot.
- Dicho el punto anterior, necesitaras tener añadido en tu servidor dicho bot y para empezar a programarlo tienes que tener el `token` del mismo, ya que sera por medio de este que podrás conectar y habitar el bot.

## Instrucciones de uso

1. **Instalación**. Primero debes descargar el repositorio. Crea un entorno e instala los módulos que necesita el proyecto.

   ```bash
   # clonar el repo
   git clone <enlace de repo>
   ```

   ```bash
   # crear entorno.
   python -m venv <nombre del entorno>
   ```

    ```bash
   # activa el entorno. Esto varia entre cada sistema operativo.
   # en mi caso, active desde git-bash.
   source <nombre del entorno>/Script/Activate
   ```

   ```bash
   # instalar módulos necesarios
   pip install -r documentacion/requirements.txt
   ```

    ```bash
    # crear entorno.
    python -m venv <nombre del entorno>
   ```

2. **env, token y owner**. Añade una nueva carpeta llamada `private` y añade a este mismo un archivo llamado `.env`. Este ultimo sera donde añadiremos el valor del token del bot.

   ```bash
   # crear carpeta y archivo
    mkdir private
    touch private/.env
   ```

    Abre el archivo .env y añade una variable llamada `DISCORD_TOKEN` y le asignas el token del bot entre comillas.

   ```bash
   # DISCORD_TOKEN = '<token de tu bot>'
   ```

    También añade la variable `OWNER_ID` y el dato que le debes proporcionar sera tu id de tu usuario de discord. Esto con la finalidad de comandos como el `>disconnect` del bot, no sean ejecutados por cualquier unario. La id debe ser un dato numérico.

   ```bash
   # OWNER_ID = <id de discord>
   ```

3. Si seguiste las indicaciones correctamente, el bot esta listo para trabajar. Solo ejecuta el script ``main.py`` en tu terminal y el bot empezara a trabajar.

   Para apagar el bot puedes cerrar la terminal o ejecutar el comando desde discord `>disconnect`.

****
