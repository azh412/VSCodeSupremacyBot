import discord
import os
from replit import db
client = discord.Client()

@client.event
async def on_ready():
  print(f'VSCODE PREACHER AS {client.user}')

@client.event
async def on_message(message):
  try:
    if message.author == client.user:
      return
    mes = message.content.lower()
    words = mes.split()
    editors = db.keys()
    if words[0] == "!@#$%^&*()editor":
      try:
        db[f"{words[1]}"] = 0
        await message.channel.send(f"{words[1]}, hm.")
      except:
        pass
    if words[0] == "!@#$%^&*()editors":
      await message.channel.send(editors)
    for i in words:
      if i in editors:
        await message.channel.send("VSCODE SUPREMACY.")
        return
  except:
    print("some error occured")
client.run(os.getenv("TOKEN"))