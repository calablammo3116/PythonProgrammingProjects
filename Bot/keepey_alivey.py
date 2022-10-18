# This program is a side program to create a web server for the bot and then keep it running continuously,
# EVEN after the tab running the bot (in "Replit," or "Repl.it," as it used to be called) is closed. This will allow it to be a TRUE
# functioning Discord bot. Thankfully, it is not too hard at all to do. We simply need to make a "Flask" server by using the Python module "Flask." 
# This will enable us to create a web server for the bot. HOWEVER, after 1 hour of not being used, this web server will enter a "sleeping" state,
# and we will subsequently see the bot stop running. To work around this issue, we will use a free website service from "uptimerobot.com" to continuously ping the Discord bot's web server,
# once every user-specified interval (e.g. once every 30 minutes). This will enable the Discord bot to run continuously WITHOUT requiring any maintenance. 
# How cool is that!? Good luck! You got this!

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()