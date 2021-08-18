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
    file.close()
@bot.event
async def on_ready():
    print('Bot is up')

@bot.command(name='neofetch')
async def neofetch(ctx):
    await ctx.send("```please wait for 5 seconds, processing your input```")
    x = subprocess.Popen('neofetch --stdout > /path', stdout=subprocess.PIPE, shell=True)
    time.sleep(5)
    file = open ("/path", "r")
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

@bot.command(name='remindme')
async def remindme(ctx, time_here, *, reason):
    userID = ctx.message.author.id
    time_here = int(time_here)
    new_time = datetime.now() + timedelta(hours=time_here)
    bot.loop.create_task(RemindFunction(userID, new_time, reason))
    time.sleep(5)
    json_file = open("database.json", "r")
    final_file = json.load(json_file)
    print(final_file[f'{ctx.message.author.id}'])
    variable_defined = final_file[f'{ctx.message.author.id}']

    
        
    if variable_defined is not None:
        try:
            await ctx.send(variable_defined['time'])
            time_to_remind = variable_defined['time']
        except KeyError:
            await ctx.send("Invalid")
            
    now = datetime.now()
    while time_to_remind is not None:
        if now.strftime("%H %d %m %Y") >= time_to_remind:
            await ctx.send(f'hello {ctx.author.mention}, you asked me to remind you for {reason}')
            break 
        else:
            continue
        time.sleep(5)

bot.run("")
