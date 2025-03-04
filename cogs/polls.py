import discord
from discord.ext import commands
import asyncio

class PollsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll")
    async def create_poll(self, ctx, question: str, *options):
        if not question or not options:
            await ctx.send("❌ Invalid arguments! Use: `!poll <question> <option1> <option2> ... [time]`")
            return
        if len(options) < 2:
            await ctx.send("❌ You need at least **two options** to create a poll!")
            return
        if len(options) > 10:
            await ctx.send("❌ Polls can have a maximum of **10 options**.")
            return

        try:
            poll_duration = int(options[-1]) 
            options = options[:-1] 
        except:
            poll_duration = None  

        description = f"**{question}**\n\n"
        count = 1
        for option in options:
            description += f"{count}️⃣ {option}\n"
            count += 1

        embed = discord.Embed(title="📊 New Poll!", description=description, color=discord.Color.blue())

        # Set footer with time info
        if poll_duration:
            embed.set_footer(text=f"Poll created by {ctx.author.display_name} | Ends in {poll_duration} seconds")
        else:
            embed.set_footer(text=f"Poll created by {ctx.author.display_name}")

        poll_message = await ctx.send(embed=embed)

        reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        for i in range(len(options)):
            await poll_message.add_reaction(reactions[i])

        if poll_duration:
            await asyncio.sleep(poll_duration)
            poll_message = await ctx.channel.fetch_message(poll_message.id)  

            results = {}
            for i, reaction in enumerate(poll_message.reactions):
                if i < len(options):
                    results[options[i]] = reaction.count - 1  

            all_zero = True
            for votes in results.values():
                if votes > 0:
                    all_zero = False
                    break

            if results and not all_zero:
                max_votes = 0
                winners = []

                for option, votes in results.items():
                    if votes > max_votes:
                        max_votes = votes
                        winners = [option]  
                    elif votes == max_votes:
                        winners.append(option) 

                # Format the winner output
                if len(winners) == 1:
                    winner = winners[0] 
                else:
                    winner = ", ".join(winners) 
            else:
                winner = "No votes" 

            result_description = f"**{question}**\n\n"
            for option, votes in results.items():
                result_description += f"✅ {option}: **{votes}** votes\n"

            result_description += f"\n🎉 **Winner:** {winner}"

            embed.title = "📊 Poll Ended!"
            embed.description = result_description
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Poll ended after {poll_duration} seconds.")

            await poll_message.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(PollsCog(bot))
