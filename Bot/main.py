# For this bot, our goal is to create a bot that can read a user's nickname and then determine if an individual string in it matches even one of the names in a massive database of real people's names. For this, we PLAN (emphasis on "PLAN," because we don't *know* if this is going to work, but I'm pretty sure it does) to use my names.py file, containing a list called "names_list" that essentially functions as a MASSIVE database of names, to compare the user's nickname against to see if it matches ANY of the names in that file, first or last. In order to separate user's nicknames into their individual components, we will use the "nameparser" module from the good contributor online (whose name I do not know at the moment, but I really appreciate you! Thank you very very much!) to separate their names into their individual components (the "nameparser" module contains functionality primarily in the "HumanName()" function to separate one's name into its individual components, including hn.title, hn.first, hn.middle, hn.last, hn.suffix, and hn.nickname). If NONE of the components of the user's nickname match ANY (using the "any()" function, which returns "True" if any of the indices in an iterable are true, or "False" if they are all false), i.e. the "any()" function returns "FALSE" for the iterable it utilizes as an argument, which will be an iterable that iterates through the ENTIRE database of names for EACH element of the user's nickname (TITLE, FIRST, MIDDLE, LAST, and NICKNAME, so except for "hn.suffix" because a suffix would just be "Jr." or "III" or something like that), THEN the bot will output a message saying, "Friendly reminder to please change your Discord nickname to your actual name. Thanks! -- your friendly neighborhood Real Name bot". And that will be all. That is all the program needs to do. Good job!


import discord
import os
import names_drnb as nm
from nameparser import HumanName
from keepey_alivey import keep_alive

def name_checker(list1, first, middle, last, title, nickname):
  for n in list1:
      # if any(list1 == first or list1 == middle or list1 == last or list1 == title or list1 == nickname):
      #  return True
      if n == (first or middle or last or title or nickname or str(first.lower()) or str(middle.lower()) or str(last.lower()) or str(title.lower()) or str(nickname.lower())):
        i = 1
        break
      # elseif any(list1 == middle):
      #  return True
      # elseif any(list1 == last):
      # return True
      else:
        i = 0
  if i == 1:
    return True
  if i == 0:
    return False

name_l = nm.namey()
name_ll = nm.lnamey()
name_ul = nm.unamey()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    # Parse the user's nickname into its individual components
    user_nick = HumanName(message.author.nick)

    # If any name in nm.namey("names.txt") matches any elements of the Discord user's nickname, just return. Else, print the message, "Friendly reminder to please change your Discord nickname to your actual name. Thanks! -- your friendly neighborhood Real Name bot"
    
    # if any(((name == user_nick.first) or (name == user_nick.middle) or (name == user_nick.last)) for name in name_l)
    #     return
    if name_checker(name_l, user_nick.first, user_nick.middle, user_nick.last, user_nick.title, user_nick.nickname):
      return
    elif name_checker(name_ll, user_nick.first, user_nick.middle, user_nick.last, user_nick.title, user_nick.nickname):
      return
    elif name_checker(name_ul, user_nick.first, user_nick.middle, user_nick.last, user_nick.title, user_nick.nickname):
      return
    else:
        await message.channel.send('''Hello! Friendly reminder to please change your Discord
        nickname to your actual name. Thanks! -- your friendly neighorhood robot Brandon''')

keep_alive()

client.run(os.getenv('TOKEN'))
# my_secret = os.environ['TOKEN']  <-- alternative method to get the environment variable

# ^^python discord bot code above ^^
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#   return "Bot up and running"
# if __name__ == '__main__':
#   app.run(host="0.0.0.0",debug=True,port=8080)