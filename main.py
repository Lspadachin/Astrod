import os, nextcord
import database
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
nextcord.member = True

def prefixCambiante(bot: commands.Bot, msg: nextcord.Message):
    if msg.author == bot.user:
        return
    prefijo = "!"
    datos = database.buscarserv(msg)
    if datos != None:
        prefijo = datos["prefijo"]
    return prefijo
    
nextcord.member = True
bot = commands.Bot(command_prefix=prefixCambiante,intents = (nextcord.Intents.all()),case_insensitive=True,help_command=None)

class ComandosCogs():
    @bot.command()
    @has_permissions(administrator=True)
    async def load(ctx,extension): #cargar un cog nuevo
        if ctx.author.id != 945454188400377878:
            return
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"La extensión **{extension}** ha sido cargada")

    @bot.command()
    @has_permissions(administrator=True)
    async def unload(ctx,extension): #descargar un cog que esta en funcionamiento
        if ctx.author.id != 945454188400377878:
            return
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"La extensión **{extension}** ha sido descargada")

    @bot.command()
    @has_permissions(administrator=True)
    async def reload(ctx,extension): #recargar un cog que esta en funcionamiento
        if ctx.author.id != 945454188400377878:
            return
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"La extensión **{extension}** ha sido recargada")

for archivo in os.listdir("./cogs"): #Cargar todos los cogs que se encuentren al iniciar el bot
    if archivo.endswith(".py"):
        bot.load_extension(f"cogs.{archivo[:-3]}")
        #bot.load_extension(f"cogs.cogs")

token = str(os.environ['token'])
bot.run(token)