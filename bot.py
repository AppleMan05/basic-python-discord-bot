import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from googlesearch import search
import praw
import random
import python_weather
import time

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0')

@client.event
async def on_ready():
    print("Bot is up")

guild_ids = [706385454500413470]

@slash.slash(name="ping", description="Check the bot's latency.", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')

@slash.slash(name="google", description="Google search!", options=[create_option(name="query", description="text to google", option_type=3, required=True)], guild_ids=guild_ids)
async def _google(ctx, query:str):
        await ctx.defer()
        searchContent = ""
        embed = discord.Embed(title="Google search result", color = discord.Color.blue())
        output2 = search(query, stop=12)
        #await ctx.send("test")
        for j in output2:
                if j.startswith("/search"):
                    print("3")
                    continue
                embed.add_field(name="Result", value=j, inline=False)
        await ctx.send(content=None, embed=embed)

@slash.slash(name="Weather", description="checks weather in your city!", options=[create_option(name="city", description="City name", option_type=3, required=True)], guild_ids=guild_ids)
async def _weather(ctx, city:str):
    embed = discord.Embed(title=f"Weather for {city}", color=discord.Color.green())
    weather_client = python_weather.Client()
    weather = await weather_client.find(city)
    embed.add_field(name="Temperature", value=f'{weather.current.temperature}°C, {weather.current.sky_text}\n Humidity = {weather.current.humidity}%', inline=False)
    
#    for forecast in weather.forecasts:
#        embed.add_field(name=forecast.date, value=f'{forecast.sky_text}, {forecast.temperature}', inline=True)
    await ctx.send(content=None, embed=embed)
    await weather_client.close()

@slash.slash(name="Meme", description="Gets random memes from reddit!", guild_ids=guild_ids)
async def _meme(ctx):
    await ctx.defer()
    #time.sleep(2)
    memes_posts = reddit.subreddit('memes').hot()
    post_to_pick=random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_posts if not x.stickied)
    embed=discord.Embed(title=submission.title, url=submission.url)
    #print(submission.url)
    embed.set_image(url=submission.url)
    await ctx.send(embed=embed)
client.run("")