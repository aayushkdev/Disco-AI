from discord.ext import commands, tasks
import re
from datetime import datetime, timedelta

class RemindersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminders = {}
        self.check_reminders.start()

    def parse_duration(self, duration):
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

    @commands.command(name="remindme")
    async def set_reminder(self, ctx, duration, *, message):
        time_delta = self.parse_duration(duration)
        if not time_delta:
            await ctx.send("❌ Invalid format! Use: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).")
            return

        reminder_time = datetime.now() + time_delta
        self.reminders.setdefault(ctx.author.id, []).append((reminder_time, message, ctx.channel.id))

        await ctx.send(f"✅ Reminder set for <@{ctx.author.id}> in **{duration}**!")

    @commands.command(name="reminders")
    async def list_reminders(self, ctx):
        """Lists all active reminders for the user."""
        user_reminders = self.reminders.get(ctx.author.id, [])
        if not user_reminders:
            await ctx.send("📌 You have no active reminders.")
            return
        
        reminder_list = ""
        count = 1
        for reminder in user_reminders:
            time, message, _ = reminder
            reminder_list += f"{count}. {time.strftime('%Y-%m-%d %H:%M')} - {message}\n"
            count += 1
        
        await ctx.send(f"📅 **Your Active Reminders:**\n{reminder_list}")

    @commands.command(name="delreminder")
    async def delete_reminder(self, ctx, index):
        user_reminders = self.reminders.get(ctx.author.id, [])
        if 1 <= index <= len(user_reminders):
            del user_reminders[index - 1]
            await ctx.send("🗑️ Reminder deleted successfully!")
        else:
            await ctx.send("❌ Invalid reminder index!")

    @commands.command(name="modifyreminder")
    async def modify_reminder(self, ctx, index, new_duration, *, new_message):
        user_reminders = self.reminders.get(ctx.author.id, [])
        if 1 <= index <= len(user_reminders):
            time_delta = self.parse_duration(new_duration)
            if not time_delta:
                await ctx.send("❌ Invalid format! Use: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).")
                return
            
            reminder_time = datetime.now() + time_delta
            user_reminders[index - 1] = (reminder_time, new_message, ctx.channel.id)
            await ctx.send(f"✏️ Reminder updated for <@{ctx.author.id}> in **{new_duration}**!")
        else:
            await ctx.send("❌ Invalid reminder index!")

    @tasks.loop(seconds=30)
    async def check_reminders(self):
        now = datetime.now()
        for user_id, user_reminders in list(self.reminders.items()):
            for reminder in user_reminders[:]:
                reminder_time, message, channel_id = reminder
                if reminder_time <= now:
                    channel = self.bot.get_channel(channel_id)
                    if channel:
                        await channel.send(f"⏰ <@{user_id}>, Reminder: {message}")
                    user_reminders.remove(reminder)
            if not user_reminders:
                del self.reminders[user_id]

    @set_reminder.error
    @delete_reminder.error
    @modify_reminder.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            command_usage = {
                "remindme": "`!remindme <time> <message>`",
                "delreminder": "`!delreminder <index>`",
                "modifyreminder": "`!modifyreminder <index> <new time> <new message>`",
            }
            await ctx.send(f"❌ Invalid arguments! Correct usage: {command_usage.get(ctx.command.name)}")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("❌ Invalid input! Please check your arguments and try again.")

async def setup(bot):
    await bot.add_cog(RemindersCog(bot))
