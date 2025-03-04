import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        server_icon = ctx.guild.icon.url if ctx.guild.icon else None
        
        embed = discord.Embed(title="📖 Help Menu", description="List of available commands:", color=discord.Color.blue())
        embed.set_thumbnail(url=server_icon)  
        
        embed.add_field(name="🤖 AI Chat Commands", value=
            "You can chat with the AI by **mentioning the bot** in a message.\n"
            "Example: `@Disco-AI How do I use Python?`\n"
            "The AI will respond with a concise answer!\n\n",
            inline=False)
        
        embed.add_field(name="📊 Poll Commands", value=
            "`!poll <question> <option1> <option2> ... [time]` - Create a poll.\n"
            "Example: `!poll 'Favorite Band?' AC/DC Metallica Nirvana 1d2h`\n"
            "Polls can have up to 10 options and an optional time limit.\n"
            "Time format: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).\n\n",
            inline=False)
        
        embed.add_field(name="⏰ Reminder Commands", value=
            "`!remindme <time> <message>` - Set a reminder.\n"
            "Time format: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).\n"
            "Example: `!remindme 1h30m Walk the dog`\n\n"
            "`!reminders` - List active reminders.\n"
            "`!delreminder <index>` - Delete a reminder by index.\n"
            "`!modifyreminder <index> <new time> <new message>` - Modify an existing reminder.", inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
