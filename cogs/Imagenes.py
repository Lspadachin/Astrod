from nextcord.ext import commands

class Imagenes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def imagenes(self, num):
        enlaces = [
            "https://cdn.discordapp.com/attachments/983447873830129675/983846217207386132/Palomita.png",#000
            "https://cdn.discordapp.com/attachments/983447873830129675/983845797399515136/Advertencia.png",#001
            "https://cdn.discordapp.com/attachments/983447873830129675/983846105475350558/Negacion1.png",#002
            "https://cdn.discordapp.com/attachments/983447873830129675/984968779433922560/Enojado.png",#003
            "https://cdn.discordapp.com/attachments/983447873830129675/983869245437907004/Ping.png",#004
            "https://cdn.discordapp.com/attachments/983447873830129675/994434582407549038/anonimo.png",#005
            "https://cdn.discordapp.com/attachments/983447873830129675/984968414307172392/Robot.png",#006
            "https://cdn.discordapp.com/attachments/983447873830129675/983845855385759825/Feliz2.png",#007
            "https://cdn.discordapp.com/attachments/983447873830129675/984968820483588096/Entrada.png",#008
            "https://cdn.discordapp.com/attachments/983447873830129675/983846031491997746/Salida.png",#009
            "https://cdn.discordapp.com/attachments/983447873830129675/994682517489729638/Triste.png",#010
            "https://cdn.discordapp.com/attachments/983447873830129675/1000171481692643328/Astrals.png",#011
            "https://cdn.discordapp.com/attachments/1000131146253873193/1000131315246571600/Python.jpg",#012
            "https://cdn.discordapp.com/attachments/983447873830129675/1001950882780426240/Mundo.png",#013
            "https://cdn.discordapp.com/attachments/983447873830129675/1001958982883225650/Discord.png",#014
            "https://cdn.discordapp.com/attachments/983447873830129675/1001961770967126016/Libro.png",#015
            "https://cdn.discordapp.com/attachments/983447873830129675/1004146291397374073/Comandos.png",#016
            "https://cdn.discordapp.com/attachments/983447873830129675/1004148579612500068/arroba.png"#017
      
        ]
        return enlaces[num]
    def gifs(self, num):
        enlaces = [
            "https://cdn.discordapp.com/attachments/983447873830129675/983846217207386132/Palomita.png",#000
        ]
        return enlaces[num]

def setup(bot):
  bot.add_cog(Imagenes(bot))