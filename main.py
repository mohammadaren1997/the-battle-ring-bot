import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# بعداً بقیه کامندها و کنترل بازی به اینجا اضافه می‌شه

bot.run("YOUR_BOT_TOKEN")
