import discord
from discord.ext import commands, tasks
import re
from datetime import datetime, timedelta, timezone

class PollsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.polls = {}  
        self.check_polls.start()

    def parse_duration(self, duration: str):
        """Parses duration like '1y2mo3w4d5h6m7s' into a timedelta."""
        time_units = {
            "y": 365 * 24 * 60 * 60, 
            "mo": 30 * 24 * 60 * 60,
            "w": 7 * 24 * 60 * 60,  
            "d": 24 * 60 * 60,   
            "h": 60 * 60,         
            "m": 60,                  
            "s": 1               
        }

        total_seconds = 0
        matches = re.findall(r"(\d+)(y|mo|w|d|h|m|s)", duration)

        for value, unit in matches:
            total_seconds += int(value) * time_units[unit]

        return timedelta(seconds=total_seconds) if total_seconds > 0 else None

    @commands.command(name="poll")
    async def create_poll(self, ctx, question: str, *options):
        """Creates a new poll with a duration using y, mo, w, d, h, m, s format."""
        if len(options) < 2:
            await ctx.send("❌ You need at least **two options** to create a poll!")
            return
        if len(options) > 10:
            await ctx.send("❌ Polls can have a maximum of **10 options**.")
            return

        poll_duration = None
        if re.match(r"^\d+[ymowdhs]+$", options[-1]):  
            poll_duration = self.parse_duration(options[-1])
            options = options[:-1]

        if not poll_duration:
            await ctx.send("❌ Invalid duration format! Use: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).")
            return

        end_time = datetime.now(timezone.utc) + poll_duration
        description = f"**{question}**\n\n"
        for i, option in enumerate(options, start=1):
            description += f"{i}️⃣ {option}\n"

        embed = discord.Embed(title="📊 New Poll!", description=description, color=discord.Color.blue())
        embed.set_footer(text=f"Poll created by {ctx.author.display_name} | Ends on {end_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")

        poll_message = await ctx.send(embed=embed)

        reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        for i in range(len(options)):
            await poll_message.add_reaction(reactions[i])

        self.polls[poll_message.id] = (end_time, question, options, poll_message.channel.id)

    @tasks.loop(seconds=30)
    async def check_polls(self):
        now = datetime.now(timezone.utc)
        for poll_id, poll_data in list(self.polls.items()):
            end_time, question, options, channel_id = poll_data
            if end_time <= now:
                channel = self.bot.get_channel(channel_id)
                if channel:
                    poll_message = await channel.fetch_message(poll_id)
                    results = {options[i]: reaction.count - 1 for i, reaction in enumerate(poll_message.reactions) if i < len(options)}

                    max_votes = max(results.values(), default=0)
                    winners = [option for option, votes in results.items() if votes == max_votes] if max_votes > 0 else ["No votes"]

                    result_description = f"**{question}**\n\n"
                    for option, votes in results.items():
                        result_description += f"✅ {option}: **{votes}** votes\n"
                    result_description += f"\n🎉 **Winner:** {', '.join(winners)}"

                    embed = discord.Embed(title="📊 Poll Ended!", description=result_description, color=discord.Color.green())
                    embed.set_footer(text=f"Poll ended on {now.strftime('%Y-%m-%d %H:%M:%S UTC')}.")

                    await poll_message.edit(embed=embed)

                del self.polls[poll_id]

    @create_poll.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Invalid arguments! Correct usage: `!poll <question> <option1> <option2> ... [duration]`")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Invalid input! Please check your arguments and try again.")

async def setup(bot):
    await bot.add_cog(PollsCog(bot))
