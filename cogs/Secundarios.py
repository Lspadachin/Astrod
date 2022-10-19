from nextcord.ext import commands

class Secundarios(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        cogImagenes = self.bot.get_cog("Imagenes")
        cogEmbeds = self.bot.get_cog("Embeds")
        
        latencia = int((self.bot.latency)*1000)
        color = 0x00ff36
        imagen1 = cogImagenes.imagenes(16)
        imagen2 = cogImagenes.imagenes(4)
        imagenfinal = cogImagenes.imagenes(0)
        titulo = "Ping"
        descripcion = "La latencia del bot es de **"+str(latencia)+"ms**"
        tiempo = True
        msgfinal = f"Ese es mi ping {ctx.author.name}"
        
        await cogEmbeds.respuesta(ctx, color, imagen1, titulo, descripcion, imagen2, tiempo, msgfinal, imagenfinal)

def setup(bot):
    bot.add_cog(Secundarios(bot))