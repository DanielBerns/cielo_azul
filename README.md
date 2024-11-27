# cielo_azul
Práctica con la API de bsky - Playing with bsky api

## Instalación - Instalation

sp: Ejecutar los siguientes comandos en la línea de comandos para instalar el demo cielo_azul 
en: Run the following commands on the command line to install the cielo_azul demo

> cd ~
> mkdir ~/projects
> cd ~/projects
> git clone https://github.com/DanielBerns/cielo_azul.git
> cd cielo_azul
> mkdir ~/.venvs/
> python -m venv ~/.venvs/bsky
> . ~/.venvs/bsky/bin/activate
> pip install -r ./requirements.txt

## Ejecución de los demos

Es necesario tener un usuario y contraseña en https://bsky.app/

> cd ~/projects/cielo_azul/demo
> . ~/.venvs/bsky/bin/activate
> python demo_send_post.py user password
> python demo_send_images.py user password
