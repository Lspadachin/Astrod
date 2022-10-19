import nextcord, datetime, database
from nextcord.ext import commands

class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def principal(ctx, color, imagen1, titulo, descripcion, imagen2, tiempo, msgfinal, imagenfinal):
        if color == None:
            color = 0xb4b4b4
        principalEmbed = nextcord.Embed(description = descripcion, color = color)
        principalEmbed.set_author(name= titulo, icon_url = imagen1)
        if imagen2 != None:
            principalEmbed.set_thumbnail(url=imagen2)
        if tiempo == True:
            principalEmbed.timestamp = datetime.datetime.now()
        principalEmbed.set_footer(text=msgfinal, icon_url=imagenfinal)
        """Colocar para la imagen final llamada a la funcion que de la imagen del bot si es None"""
        return principalEmbed

    async def respuesta(self, ctx, color, imagen1, titulo, descripcion, imagen2, tiempo, msgfinal, imagenfinal):
        principalEmbed = Embeds.principal(ctx, color, imagen1, titulo, descripcion, imagen2, tiempo, msgfinal, imagenfinal)
        respuesta = database.buscardatousr(ctx, "respuesta")
        if respuesta == True:
            try: #Buscar el mensaje en ctx para responderlo
                mensaje = ctx.message
                await mensaje.reply(embed=principalEmbed)
            except: #Responder al ctx directo en caso de no encontrar mensaje
                await ctx.reply(embed=principalEmbed)
        else:
            canal = ctx.message
            await canal.send(embed=principalEmbed)
            #
def setup(bot):
    bot.add_cog(Embeds(bot))