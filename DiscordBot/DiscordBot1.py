from discord import message
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
from discord.message import Message
import requests
import json
import re


prefix=commands.Bot(command_prefix="^")
reg = r"^[iI]'?a?[mM] "



@prefix.event
async def on_ready():
    print('Ready!')

@prefix.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Oh no! Something went wrong! Use ^Help for correct spelling")

@prefix.event
async def on_message(message):
    if prefix.user.id != message.author.id:
        if re.match(reg,message.content):
            await message.channel.send("Hi {0}, I'm Dad!".format(re.sub(reg, "", str(message.content))))
    await prefix.process_commands(message)





@prefix.command()
async def advice(ctx):
    URL = "https://api.adviceslip.com/advice"
    r = requests.get(url= URL)
    unga = r.text
    obj = json.loads(str(unga))
    await ctx.send(str(obj["slip"]["advice"]))



    

@prefix.command()
async def joke(ctx):
    URL = "https://icanhazdadjoke.com/"
    header={

        "Accept":"application/json"
    }
    yap=requests.get(url=URL,headers=header)
    obj = json.loads(str(yap.text))
    await ctx.send(str(obj["joke"]))










#yes
#yes again

prefix.run('ODQ0NzU4Mjc4NjA5MTc0NTI5.YKXEdA.gfCAHdHxDBYotPmB5XP9i-pQ6ck')