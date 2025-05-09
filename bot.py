import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(commands.when_mentioned_or("!"), intents=intents, case_insensitive=True, help_command=None,)

initial_extensions = [ 
    "cogs.welcome", 
    "cogs.polls",
    "cogs.reminders",
    "cogs.help",
    "cogs.chat",
]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for ext in initial_extensions:
        print(f"loaded {ext}")
        await bot.load_extension(ext)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  
    raise error  

bot.run(TOKEN)
