# app/comandos.py

import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
import pytz

class ScheduledMessage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()
        self.scheduler.add_job(self.send_embed_message, CronTrigger(hour=13, minute=1, second=30, timezone=pytz.timezone('America/Mexico_City')))
        self.scheduler.start()

    async def send_embed_message(self):
        channel_id = 1233924399862644758 
        role_id = 1244393242653495359
        voice_channel_id = 1231693494330982428
        role_mention = f'<@&{role_id}>'
        voice_channel_mention = f'<#{voice_channel_id}>'
        channel = self.bot.get_channel(channel_id)
        
        if channel:
            embed = discord.Embed(
                title="Papu, tienes una video llamada de Python 🗣️", 
                description=f"{role_mention}. Recuerden que tenemos reunión dentro de **1 HORA** por el canal de voz {voice_channel_mention} .  La hora local a la que empiezan las sesiones son a las : <t:1716926400:t> o lo que es equivalente a las 2pm hora ciudad de Mexico.", 
                color=0x00ff00
            )
            
            # Asegúrate de que la URL de la imagen sea válida
            embed.set_image(url="https://i.postimg.cc/zvS2v5pW/banner-py.png")  # Cambia esto por una URL válida
            
            embed.set_footer(text="Martes y Jueves. 2pm MX")
            
            try:
                await channel.send(embed=embed)
                print("Mensaje enviado correctamente")
            except discord.HTTPException as e:
                print(f"Error al enviar el mensaje: {e}")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot conectado como {self.bot.user}')

def setup(bot):
    bot.add_cog(ScheduledMessage(bot))
