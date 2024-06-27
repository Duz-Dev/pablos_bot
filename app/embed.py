# app/comandos.py
from discord.ext import commands
from discord import ApplicationContext, Embed

class EmbedBuilder(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="embed", description="Envía un mensaje embed")
    async def send_embed(self, ctx: ApplicationContext, titulo: str, mensaje: str, imagen: str, pie_de_pagina: str):
        embed = Embed(title=titulo, description=mensaje, color=0x00ff00)
        embed.set_image(url=imagen)
        embed.set_footer(text=pie_de_pagina)
        await ctx.respond(embed=embed)

def setup(bot: commands.Bot): 
    bot.add_cog(EmbedBuilder(bot))
