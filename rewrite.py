import discord
from discord.ext import commands,tasks
import os
import subprocess
import time
from googlesearch import search

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is up')

@bot.command(name='neofetch')
async def neofetch(ctx):
    await ctx.send("```please wait for 5 seconds, processing your input```")
    x = subprocess.Popen('neofetch --stdout > /home/aryan/text.txt', stdout=subprocess.PIPE, shell=True)
    time.sleep(5)
    file = open ("/home/aryan/text.txt", "r")
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
    output2 = search(query, num_results=12)
    #for i in range (2, len(input)):
     #   searchContent = searchContent + input[i]
        
    embed = discord.Embed(title="Google search result")
    for j in output2:
        if j.startswith("/search"):
           continue
        embed.add_field(name="Result", value=j )
    await ctx.send(content=None, embed=embed)
bot.run("")
