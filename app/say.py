# módulos para trabajar con la api de discord
from discord.ext import commands
from discord import ApplicationContext, Member

class Say(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="say", description="Muestra un mensaje xd")
    async def say_chilito(self, ctx: ApplicationContext, usuario: Member):
        await ctx.respond(f"{usuario.mention} me toco mi chilito 😭")
    
    @commands.slash_command(name="xd", description="Muestra un xd y menciona al usuario")
    async def xd(self, ctx: ApplicationContext, usuario: Member):
        await ctx.respond(f"ola xd {usuario.mention}")
    
    @commands.command(name="saludo")
    async def saludo(self, ctx: commands.Context): 
        await ctx.reply(f"Hola {ctx.author.mention}")

def setup(bot: commands.Bot): 
    bot.add_cog(Say(bot))
