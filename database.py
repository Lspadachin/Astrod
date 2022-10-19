import os
from pymongo import MongoClient

claveconexion = str(os.environ['claveconexion'])
basededatos = MongoClient(claveconexion)

datos_servidores = basededatos["Astrod"]["Servidores"]
datos_usuarios = basededatos["Astrod"]["Usuarios"]


def abrir_servidoreserodivres_rirbaa(ctx):
    datos = datos_servidores.find_one({"id": ctx.guild.id})
    if datos == None:
        servidor = {
            "id": ctx.guild.id,
            "prefijo": "!",
            "lenguaje": "es",
            "canalEntrada": None,
            "canalSalida": None,
            "bots": True,
            "rolesServidor": list(),
            "canalesComandos": list()
        }
        datos_servidores.insert_one(servidor)
    else:
        return

def abrir_cuentaatneuc_rirbaa(user):
    datos = datos_usuarios.find_one({"id": user.id})
    if datos == None:
        nom = user.name.replace(" ", "")
        cuenta = {
            "id": user.id,
            "nombre": nom,
            "lenguaje": "es",
            "astrals": 1,
            "respuesta": True
        }
        datos_usuarios.insert_one(cuenta)
    else:
        return


def buscarserv(ctx):
    abrir_servidoreserodivres_rirbaa(ctx)
    return datos_servidores.find_one({"id": ctx.guild.id})


def buscarusr(ctx):
    abrir_cuentaatneuc_rirbaa(ctx)
    return datos_usuarios.find_one({"id": ctx.id})


def buscardatousr(ctx, busqueda):
    abrir_servidoreserodivres_rirbaa(ctx)
    abrir_cuentaatneuc_rirbaa(ctx.author)
    busqueda = str(busqueda)
    datos = buscarusr(ctx.author)
    dato = datos[busqueda]
    return dato


def buscardatosrv(ctx, busqueda):
    datos = buscarserv(ctx)
    busqueda = str(busqueda)
    dato = datos[busqueda]
    return dato