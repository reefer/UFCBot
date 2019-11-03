import discord
import requests
import re
import json
import apikey
import time
import threading
from discord.ext.commands import Bot
import asyncio
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix='$')
client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Game(name="With Dana White")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print('-' * 30)
    print('Logged in as: ')
    print(client.user)
    print('-' * 30)

def data():
    key = '?api_key=' + apikey.key
    URL = 'https://api.sportradar.us/ufc/trial/v2/en/'

    url = URL + 'rankings.json' + key
    response = requests.get(url).json()
    return response

@client.command()
async def overall(ctx):
        response = data()
        overalllist = []
        for i in range(10):
            pfpnam = response['rankings'][0]['competitor_rankings'][i]['competitor']['name']
            last, first = pfpnam.split(', ')
            pfpname = first + " " + last
            overalllist.append(pfpname)
        embed = discord.Embed(title="UFC Overall Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(overalllist[0] + "**\n") \
        + "**2.) {}".format(overalllist[1] + "**\n") \
        + "**3.) {}".format(overalllist[2] + "**\n") \
        + "**4.) {}".format(overalllist[3] + "**\n") \
        + "**5.) {}".format(overalllist[4] + "**\n") \
        + "**6.) {}".format(overalllist[5] + "**\n") \
        + "**7.) {}".format(overalllist[6] + "**\n") \
        + "**8.) {}".format(overalllist[7] + "**\n") \
        + "**9.) {}".format(overalllist[8] + "**\n") \
        + "**10.) {}".format(overalllist[9] + "**\n"),
        inline=True)

        await ctx.send(embed=embed)

@client.command()
async def flyweight(ctx):
        response = data()
        flylist = []
        for i in range(10):
            flynam = response['rankings'][1]['competitor_rankings'][i]['competitor']['name']
            last, first = flynam.split(', ')
            flyname = first + " " + last
            flylist.append(flyname)
        embed = discord.Embed(title="UFC Flyweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(flylist[0] + "**\n") \
        + "**2.) {}".format(flylist[1] + "**\n") \
        + "**3.) {}".format(flylist[2] + "**\n") \
        + "**4.) {}".format(flylist[3] + "**\n") \
        + "**5.) {}".format(flylist[4] + "**\n") \
        + "**6.) {}".format(flylist[5] + "**\n") \
        + "**7.) {}".format(flylist[6] + "**\n") \
        + "**8.) {}".format(flylist[7] + "**\n") \
        + "**9.) {}".format(flylist[8] + "**\n") \
        + "**10.) {}".format(flylist[9] + "**\n"),
        inline=True)

        await ctx.send(embed=embed)

@client.command()
async def bantamweight(ctx):
        response = data()
        banlist = []
        for i in range(10):
            bannam = response['rankings'][2]['competitor_rankings'][i]['competitor']['name']
            last, first = bannam.split(', ')
            banname = first + " " + last
            banlist.append(banname)
        embed = discord.Embed(title="UFC Bantamweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(banlist[0] + "**\n") \
        + "**2.) {}".format(banlist[1] + "**\n") \
        + "**3.) {}".format(banlist[2] + "**\n") \
        + "**4.) {}".format(banlist[3] + "**\n") \
        + "**5.) {}".format(banlist[4] + "**\n") \
        + "**6.) {}".format(banlist[5] + "**\n") \
        + "**7.) {}".format(banlist[6] + "**\n") \
        + "**8.) {}".format(banlist[7] + "**\n") \
        + "**9.) {}".format(banlist[8] + "**\n") \
        + "**10.) {}".format(banlist[9] + "**\n"),
        inline=True)

        await ctx.send(embed=embed)

@client.command()
async def featherweight(ctx):
        response = data()
        featherlist = []
        for i in range(10):
            feathernam = response['rankings'][3]['competitor_rankings'][i]['competitor']['name']
            last, first = feathernam.split(', ')
            feathername = first + " " + last
            featherlist.append(feathername)
        embed = discord.Embed(title="UFC Featherweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(featherlist[0] + "**\n") \
        + "**2.) {}".format(featherlist[1] + "**\n") \
        + "**3.) {}".format(featherlist[2] + "**\n") \
        + "**4.) {}".format(featherlist[3] + "**\n") \
        + "**5.) {}".format(featherlist[4] + "**\n") \
        + "**6.) {}".format(featherlist[5] + "**\n") \
        + "**7.) {}".format(featherlist[6] + "**\n") \
        + "**8.) {}".format(featherlist[7] + "**\n") \
        + "**9.) {}".format(featherlist[8] + "**\n") \
        + "**10.) {}".format(featherlist[9] + "**\n"),
        inline=True)

        await ctx.send(embed=embed)

@client.command()
async def lightweight(ctx):
        response = data()
        lightlist = []
        for i in range(10):
            lightnam = response['rankings'][4]['competitor_rankings'][i]['competitor']['name']
            last, first = lightnam.split(', ')
            lightname = first + " " + last
            lightlist.append(lightname)
        embed = discord.Embed(title="UFC Lightweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(lightlist[0] + "**\n") \
        + "**2.) {}".format(lightlist[1] + "**\n") \
        + "**3.) {}".format(lightlist[2] + "**\n") \
        + "**4.) {}".format(lightlist[3] + "**\n") \
        + "**5.) {}".format(lightlist[4] + "**\n") \
        + "**6.) {}".format(lightlist[5] + "**\n") \
        + "**7.) {}".format(lightlist[6] + "**\n") \
        + "**8.) {}".format(lightlist[7] + "**\n") \
        + "**9.) {}".format(lightlist[8] + "**\n") \
        + "**10.) {}".format(lightlist[9] + "**\n"),
        inline=True)

        await ctx.send(embed=embed)

@client.command()
async def welterweight(ctx):
        response = data()
        welterlist = []
        for i in range(10):
            welnam = response['rankings'][5]['competitor_rankings'][i]['competitor']['name']
            last, first = welnam.split(', ')
            welname = first + " " + last
            welterlist.append(welname)
        embed = discord.Embed(title="UFC Welterweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(welterlist[0] + "**\n") \
        + "**2.) {}".format(welterlist[1] + "**\n") \
        + "**3.) {}".format(welterlist[2] + "**\n") \
        + "**4.) {}".format(welterlist[3] + "**\n") \
        + "**5.) {}".format(welterlist[4] + "**\n") \
        + "**6.) {}".format(welterlist[5] + "**\n") \
        + "**7.) {}".format(welterlist[6] + "**\n") \
        + "**8.) {}".format(welterlist[7] + "**\n") \
        + "**9.) {}".format(welterlist[8] + "**\n") \
        + "**10.) {}".format(welterlist[9] + "**\n"),
        inline=True)

        await ctx.send(embed=embed)

@client.command()
async def middleweight(ctx):
        response = data()
        middlelist = []
        for i in range(10):
            middlenam = response['rankings'][6]['competitor_rankings'][i]['competitor']['name']
            last, first = middlenam.split(', ')
            middlename = first + " " + last
            middlelist.append(middlename)
        embed = discord.Embed(title="UFC Middleweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(middlelist[0] + "**\n") \
        + "**2.) {}".format(middlelist[1] + "**\n") \
        + "**3.) {}".format(middlelist[2] + "**\n") \
        + "**4.) {}".format(middlelist[3] + "**\n") \
        + "**5.) {}".format(middlelist[4] + "**\n") \
        + "**6.) {}".format(middlelist[5] + "**\n") \
        + "**7.) {}".format(middlelist[6] + "**\n") \
        + "**8.) {}".format(middlelist[7] + "**\n") \
        + "**9.) {}".format(middlelist[8] + "**\n") \
        + "**10.) {}".format(middlelist[9] + "**\n"),
        inline=True)



        await ctx.send(embed=embed)

@client.command()
async def lightheavyweight(ctx):
        response = data()
        lhlist = []
        for i in range(10):
            lhnam = response['rankings'][7]['competitor_rankings'][i]['competitor']['name']
            last, first = lhnam.split(', ')
            lhname = first + " " + last
            lhlist.append(lhname)
        embed = discord.Embed(title="UFC Light Heavyweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(lhlist[0] + "**\n") \
        + "**2.) {}".format(lhlist[1] + "**\n") \
        + "**3.) {}".format(lhlist[2] + "**\n") \
        + "**4.) {}".format(lhlist[3] + "**\n") \
        + "**5.) {}".format(lhlist[4] + "**\n") \
        + "**6.) {}".format(lhlist[5] + "**\n") \
        + "**7.) {}".format(lhlist[6] + "**\n") \
        + "**8.) {}".format(lhlist[7] + "**\n") \
        + "**9.) {}".format(lhlist[8] + "**\n") \
        + "**10.) {}".format(lhlist[9] + "**\n"),
        inline=True)



        await ctx.send(embed=embed)

@client.command()
async def heavyweight(ctx):
        response = data()
        heavylist = []
        for i in range(10):
            heavynam = response['rankings'][8]['competitor_rankings'][i]['competitor']['name']
            last, first = heavynam.split(', ')
            heavyname = first + " " + last
            heavylist.append(heavyname)
        embed = discord.Embed(title="UFC Heavyweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed=discord.Embed(title="UFC Heavyweight Rankings", color=0x0006fd)
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(heavylist[0] + "**\n") \
        + "**2.) {}".format(heavylist[1] + "**\n") \
        + "**3.) {}".format(heavylist[2] + "**\n") \
        + "**4.) {}".format(heavylist[3] + "**\n") \
        + "**5.) {}".format(heavylist[4] + "**\n") \
        + "**6.) {}".format(heavylist[5] + "**\n") \
        + "**7.) {}".format(heavylist[6] + "**\n") \
        + "**8.) {}".format(heavylist[7] + "**\n") \
        + "**9.) {}".format(heavylist[8] + "**\n") \
        + "**10.) {}".format(heavylist[9] + "**\n"),
        inline=True)



        await ctx.send(embed=embed)

@client.command()
async def strawweight(ctx):
        response = data()
        wstrawlist = []
        for i in range(10):
            wstrawnam = response['rankings'][9]['competitor_rankings'][i]['competitor']['name']
            last, first = wstrawnam.split(', ')
            wstrawname = last + " " + first
            wstrawlist.append(wstrawname)
        embed = discord.Embed(title="UFC Womens Strawweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")

        embed.add_field(name="-" * 25,
        value="**1.) {}".format(wstrawlist[0] + "**\n") \
        + "**2.) {}".format(wstrawlist[1] + "**\n") \
        + "**3.) {}".format(wstrawlist[2] + "**\n") \
        + "**4.) {}".format(wstrawlist[3] + "**\n") \
        + "**5.) {}".format(wstrawlist[4] + "**\n") \
        + "**6.) {}".format(wstrawlist[5] + "**\n") \
        + "**7.) {}".format(wstrawlist[6] + "**\n") \
        + "**8.) {}".format(wstrawlist[7] + "**\n") \
        + "**9.) {}".format(wstrawlist[8] + "**\n") \
        + "**10.) {}".format(wstrawlist[9] + "**\n"),
        inline=True)



        await ctx.send(embed=embed)

@client.command()
async def wflyweight(ctx):
        response = data()
        wflylist = []
        for i in range(10):
            wflynam = response['rankings'][10]['competitor_rankings'][i]['competitor']['name']
            last, first = wflynam.split(', ')
            wflyname = first + " " + last
            wflylist.append(wflyname)
        embed = discord.Embed(title="UFC Womens Flyweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(wflylist[0] + "**\n") \
        + "**2.) {}".format(wflylist[1] + "**\n") \
        + "**3.) {}".format(wflylist[2] + "**\n") \
        + "**4.) {}".format(wflylist[3] + "**\n") \
        + "**5.) {}".format(wflylist[4] + "**\n") \
        + "**6.) {}".format(wflylist[5] + "**\n") \
        + "**7.) {}".format(wflylist[6] + "**\n") \
        + "**8.) {}".format(wflylist[7] + "**\n") \
        + "**9.) {}".format(wflylist[8] + "**\n") \
        + "**10.) {}".format(wflylist[9] + "**\n"),
        inline=True)



        await ctx.send(embed=embed)

@client.command()
async def wbantamweight(ctx):
        response = data()
        wbanlist = []
        for i in range(10):
            wbannam = response['rankings'][11]['competitor_rankings'][i]['competitor']['name']
            last, first = wbannam.split(', ')
            wbanname = first + " " + last
            wbanlist.append(wbanname)
        embed = discord.Embed(title="UFC Womens Flyweight Rankings", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="-" * 25,
        value="**1.) {}".format(wbanlist[0] + "**\n") \
        + "**2.) {}".format(wbanlist[1] + "**\n") \
        + "**3.) {}".format(wbanlist[2] + "**\n") \
        + "**4.) {}".format(wbanlist[3] + "**\n") \
        + "**5.) {}".format(wbanlist[4] + "**\n") \
        + "**6.) {}".format(wbanlist[5] + "**\n") \
        + "**7.) {}".format(wbanlist[6] + "**\n") \
        + "**8.) {}".format(wbanlist[7] + "**\n") \
        + "**9.) {}".format(wbanlist[8] + "**\n") \
        + "**10.) {}".format(wbanlist[9] + "**\n"),
        inline=True)



        await ctx.send(embed=embed)

@client.command()
async def search(ctx, arg, arg1):
        name = arg + " " + arg1
        website_url = requests.get('http://en.wikipedia.org/wiki/UFC_' + arg1).text
        soup = BeautifulSoup(website_url,'html.parser')
        My_table = soup.find('table',{'class':'toccolours'})
        h = []
        for row in My_table.findAll('tr'):
            h.append(row.text.replace('\n', ' '))
        try:
            headers = h[1]
            fight1 = h[2]
            fight2 = h[3]
            fight3 = h[4]
            fight4 = h[5]
            fight5 = h[6]
            prelimcard = h[7]
            fight6 = h[8]
            fight7 = h[9]
            fight8 = h[10]
            fight9 = h[11]
            earlyprelim = h[12]
            fight10 = h[13]
            fight11 = h[14]
            fight12 = h[15]
        except:
            print('error')

        embed = discord.Embed(title="Results from " + name, colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")

        embed.add_field(name="**Main Card**",
        value="{}\n".format(headers) \
        + "{}\n".format(fight1) \
        + "{}\n".format(fight2) \
        + "{}\n".format(fight3) \
        + "{}\n".format(fight4) \
        + "{}\n".format(fight5) ,
        inline=True)

        embed.add_field(name="**Preliminary Card**",
        value="{}\n".format(headers) \
        + "{}\n".format(fight6) \
        + "{}\n".format(fight7) \
        + "{}\n".format(fight8) ,
        inline=True)

        await ctx.send(embed=embed)

@client.command()
async def events(ctx):
        embed = discord.Embed(title="UFC Events", colour=discord.Colour(0x1406EF))
        embed.set_footer(text="UFCBot Coded by eric")
        embed.add_field(name="**UFC 244: Diaz vs Masvidal**",
        value="*New York*\n" \
        + "*Sat, November 2, 2019*\n" \
        + "*Main Card: 10:00 PM (EST)*\n" \
        + "*Prelims: 8:00 PM (EST)*\n" \
        + "*Early Prelims: 6:30 PM (EST)*\n",
        inline=True)

        embed.add_field(name="**Fight Night 163**\n",
        value="*‎Moscow, Russia*\n" \
        + "*Sat, November 9, 2019*\n" \
        + "*Main Card: 2:00 PM (EST)*\n" \
        + "*Prelims: 11:00 AM (EST)*",
        inline=True)

        embed.add_field(name="**Fight Night 164**\n",
        value="*Sao Paulo, Brazil*\n" \
        + "*Sat, November 12, 2019*\n" \
        + "*Main Card: 8:00 PM (EST)*\n" \
        + "*Prelims: 5:00 PM (EST)*",
        inline=True)

        embed.add_field(name="**UFC ON ESPN 7: Overeem vs Harris**\n",
        value="*Washington, DC*\n" \
        + "*Sat, December 7, 2019*\n" \
        + "*Main Card: N/A*",
        inline=True)

        embed.add_field(name="**UFC 245: Usman vs Covington**",
        value="*Las Vegas*\n" \
        + "*Sat, December 14, 2019*\n" \
        + "*Main Card: N/A*\n" \
        + "*Prelims: N/A*\n" \
        + "*Early Prelims: N/A*",
        inline=True)

        embed.add_field(name="**Fight Night 165: Ortega vs Sung Jung**\n",
        value="*Busan, South Korea*\n" \
        + "*Sat, December 21, 2019*\n" \
        + "*Main Card: N/A*\n" \
        + "*Prelims: N/A*",
        inline=True)

        await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(colour = discord.Colour.blue()
    )
    embed.set_author(name='UFCBot Help')
    embed.add_field(name="Rankings",
    value="**$overall** \n {}".format("*Returns top 10 overall fighters as of current time.*\n") \
    + "**$flyweight**  \n {}".format("*Returns top 10 flyweight fighters as of current time.*\n") \
    + "**$bantamweight** \n {}".format("*Returns top 10 bantamweight fighters as of current time.*\n") \
    + "**$featherweight**\n {}".format("*Returns top 10 featherweight fighters as of current time.*\n") \
    + "**$lightweight**\n {}" .format("*Returns top 10 lightweight fighters as of current time.*\n") \
    + "**$welterweight**\n {}".format("*Returns top 10 welterweight fighters as of current time.*\n") \
    + "**$lightheavyweight**\n {}".format("*Returns top 10 light heavyweight fighters as of current time.*\n") \
    + "**$heavyweight**\n {}".format("*Returns top 10 heavyweight fighters as of current time.*\n") \
    + "**$strawweight**\n {}".format("*Returns top 10 womens strawweight fighters as of current time.*\n") \
    + "**$wflyweight**\n {}".format("*Returns top 10 womens flyweight fighters as of current time.*\n") \
    + "**$wbantamweight**\n {}".format("*Returns top 10 womens bantamweight fighters as of current time.*\n")),

    embed.add_field(name="Upcoming Events\n",
    value="**$events**\n {}".format("*Returns known upcoming UFC events*\n"),
    inline=True)

    embed.add_field(name="Event Result Search\n",
    value="**$search UFC <number> (Only supports UFC ATM, Fight Night in the works)**\n {}".format("*Returns UFC event results*\n"),
    inline=True)

    embed.set_footer(text="UFCBot Coded by eric")
    await ctx.author.send(embed=embed)


client.run(TOKEN)
