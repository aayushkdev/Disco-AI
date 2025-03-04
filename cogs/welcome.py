import discord
from discord.ext import commands

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = 1346412120912297995
        channel = member.guild.get_channel(channel_id)

        if channel:
            embed = discord.Embed(
                title="🎉 Welcome to the Server!",
                description=f"Hey {member.mention}, welcome to **{member.guild.name}**! 🚀\n"
                            "We're excited to have you here. Make sure to check out the rules and introduce yourself!",
                color=discord.Color.blue()
            )

            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(WelcomeCog(bot))
