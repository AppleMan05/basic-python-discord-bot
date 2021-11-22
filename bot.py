import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from googlesearch import search
import json
import python_weather

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

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
client.run("OTEyMjIyMzMzMDQ4MDY2MDg4.YZszQA.WzK5ezhA9YYvRUn2oLPn079Xj7Q")