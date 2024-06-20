from discord.ext import commands

class Prueba(commands.Cog):
    
    def __init__(self,bot) -> None:
        self.bot = bot
    
    @commands.command("despedida")
    async def despedida(self, ctx: commands.Context):
        await ctx.reply(f"Adios {ctx.author.mention}")
    
    @commands.command("desconexion")
    @commands.is_owner()
    async def desconexion(self,ctx: commands.Context): #el contexto recibe toda la información del mismo comando.
        await ctx.reply(f"desconectando a {self.bot.user.name}")
        await self.bot.close()

def setup(bot: commands.Bot): 
    bot.add_cog(Prueba(bot))