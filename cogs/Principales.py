import nextcord
from nextcord.ext import commands

class Principales(commands.Cog):
  
    def __init__(self, bot):
        self.bot = bot
        
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        #print(f"{bot.user.name}{bot.user.id} está aquí")
        #on_ready ha sido anulado debido al uso de prefijo cambiante
        print("\033[32m"+"{0.user} ha sido encendido.".format(self.bot))
        actividad = nextcord.Game(name="!Astrod")
        await self.bot.change_presence(status=nextcord.Status.online,activity=actividad)

    @commands.Cog.listener()
    async def on_message(self, mensaje):
        if mensaje.author == self.bot.user:
            return
        id = (mensaje.id)
        canal = mensaje.channel
        msg = await canal.fetch_message(id)
        if str(msg.content.lower()) == "hola":
            await mensaje.reply("Hola")
            
def setup(bot):
    bot.add_cog(Principales(bot))