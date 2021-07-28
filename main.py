import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from random import randint

client = discord.Client()

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

@client.command(aliases=['pedra_papel_tesoura', 'jkp'])
async def ppt(ctx, frase: str = ""):
    try:
        frase = frase.strip()
        if(frase != ""):
            if(frase == "help"):
                await ctx.send("Esse é um jogo de pedra, papel e tesoura\nPara jogar utilize >ppt <objeto>\nTroque <objeto> por 'pedra', 'papel' ou 'tesoura'")
            elif(frase == "pedra" or frase == "papel" or frase == "tesoura"):
                # 0 = pd 1 = pp 2 = ts
                x = randint(0, 2)
                if(x == 0):
                  if(frase == "pedra"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **pedra**\n**Resultado:** O jogo terminou empatado")
                  if(frase == "papel"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **pedra**\n**Resultado:** {ctx.author.mention} ganhou")
                  if(frase == "tesoura"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **pedra**\n**Resultado:** {client.user.mention} ganhou")
                elif(x == 1):
                  if(frase == "papel"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **papel**\n**Resultado:** O jogo terminou empatado")
                  if(frase == "tesoura"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **papel**\n**Resultado:** {ctx.author.mention} ganhou")
                  if(frase == "pedra"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **papel**\n**Resultado:** {client.user.mention} ganhou")
                elif(x == 2):
                  if(frase == "tesoura"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **tesoura**\n**Resultado:** O jogo terminou empatado")
                  if(frase == "pedra"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **tesoura**\n**Resultado:** {ctx.author.mention} ganhou")
                  if(frase == "papel"):
                    await ctx.send(f"{ctx.author.mention} jogou: **{frase}**\n{client.user.mention} jogou: **tesoura**\n**Resultado:** {client.user.mention} ganhou")
            else:
                await ctx.send("Objeto do pedra, papel e tesoura não reconhecido")
        else:
          await ctx.send("Esse é um jogo de pedra, papel e tesoura\nPara jogar utilize >ppt <objeto>\nTroque <objeto> por 'pedra', 'papel' ou 'tesoura'")
    except:
        await ctx.send("Um erro ocorreu")


client.run(os.getenv("TOKEN"))
