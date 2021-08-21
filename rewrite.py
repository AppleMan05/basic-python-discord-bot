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



@bot.command(name='remindme')
async def remindme(ctx, time_here, *, reason):
    if time_here is None:
        await ctx.send("No time provided")
    
    elif time_here.lower().endswith("s"):
        a = time_here.split("s")
        time.sleep(int(a[0]))
        await ctx.send(f'{ctx.author.mention} you asked me to remind you for: {reason}')
    elif time_here.lower().endswith("m"):
        a = time_here.split("m")
        time.sleep(int(a[0]) * 60)
        await ctx.send(f'{ctx.author.mention} you asked me to remind you for: {reason}')
    elif time_here.lower().endswith("h"):
        a = time_here.split("h")
        time.sleep(int(a[0]) * 60 * 60)
        await ctx.send(f'{ctx.author.mention} you asked me to remind you for: {reason}')
    else:
        await ctx.send("Invalid input")



        
    

bot.run("")
