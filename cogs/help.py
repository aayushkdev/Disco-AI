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
        
        embed.add_field(name="📊 Poll Commands", value=
            "`!poll <question> <option1> <option2> ... [time]` - Create a poll.\n"
            "Example: `!poll 'Favorite Band?' AC/DC Metallica Nirvana 30`\n"
            "Polls can have up to 10 options and an optional time limit.\n\n", inline=False)
        

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
