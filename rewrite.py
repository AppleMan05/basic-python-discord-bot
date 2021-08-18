import discord
from discord.ext import commands,tasks
import os
import subprocess
import time
from googlesearch import search
import json
from datetime import datetime, timedelta

client = discord.Client()
bot = commands.Bot(command_prefix='!')

async def RemindFunction(user_id, time, reason):
    my_dictionary = {
        user_id : {
            "time": time.strftime("%H %d %m %Y"),
            "reason": reason
        }
    }
    file = open("database.json", "w")
    json.dump(my_dictionary, file)
@bot.event
async def on_ready():
    print('Bot is up')

@bot.command(name='neofetch')
async def neofetch(ctx):
    await ctx.send("```please wait for 5 seconds, processing your input```")
    x = subprocess.Popen('neofetch --stdout > /path/to/file', stdout=subprocess.PIPE, shell=True)
    time.sleep(5)
    file = open ("/path/to/file", "r")
    output = ""
    for line in file.readlines():
        output += line
    embed = discord.Embed(title="Neofetch")
    embed.add_field(name="Output", value=output)
    await ctx.send(content=None, embed=embed)

@bot.command(name='google')
async def google(ctx, *, query):
    #input = str(query.split())
    searchContent = ""
    output2 = search(query, stop=12)
    print(output2)
    print("1")
    #for i in range (2, len(input)):
     #   searchContent = searchContent + input[i]
        
    embed = discord.Embed(title="Google search result")
    print("2")
    for j in output2:
        if j.startswith("/search"):
            print("3")
            continue
        embed.add_field(name="Result", value=j)
    await ctx.send(content=None, embed=embed)

#@bot.command(name='remindme')
#async def remindme(ctx, time, reason):
 #   userID = ctx.message.author.id
  #  time = int(time)
  #  new_time = datetime.now() + timedelta(hours=time)
  #  bot.loop.create_task(RemindFunction(userID, new_time, reason))


bot.run("")
