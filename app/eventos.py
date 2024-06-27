from discord.ext import commands

class Eventos(commands.Cog):
    
    def __init__(self,bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_connect(self): #Evento que indica cuando se realizo conexión explícitamente con discord, pero no significa que ya se puede usar.
        print("Se estableció conexión con discord 🗣️")#conexión

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user.name} esta listo para trabajar.")#listo para operar

    @commands.Cog.listener()
    async def on_disconnect(self):
        print(f"{self.bot.user.name} a terminado de trabajar.")#listo para operar

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        # Uso de un comando solo disponible para el propietario del bot
        if isinstance(error, commands.NotOwner):
            await ctx.reply(f"Solo el Admin puede hacer uso de este comando.")

def setup(bot: commands.Bot):
    bot.add_cog(Eventos(bot))