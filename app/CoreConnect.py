from discord.ext import commands

class CoreConnect(commands.Cog):
    
    def __init__(self,bot) -> None:
        self.bot = bot

    #Apaga el bot desde el server
    @commands.command("disconnect") 
    @commands.is_owner() #Define que solo el owner puede usarlo
    async def disconnect(self,ctx: commands.Context): #la función como tal
        await ctx.reply(f"desconectando a {self.bot.user.name}") #mensaje de salida
        await self.bot.close()

def setup(bot: commands.Bot): 
    bot.add_cog(CoreConnect(bot))