import discord
from discord.ext import commands
import google.generativeai as genai
import os

class GeminiChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    async def get_gemini_response(self, prompt):
        try:
            model = genai.GenerativeModel("gemini-2.0-flash")
            full_prompt = (
                "You are a helpful and concise AI assistant in a Discord server. "
                "Respond briefly (under 100 words) in a friendly and engaging tone. "
                "The bot prefix is `!`, and the available commands are: `!poll` , `!reminder`, `!help`, etc. "
                "If asked about commands, refer to this list. Avoid long explanations unless necessary. "
                "Keep responses natural and conversational.\n\n"
                f"User: {prompt}\n"
                "AI:"
            )
            response = model.generate_content(full_prompt)
            return response.text if response.text else "I couldn't generate a response."
        except Exception as e:
            return f"Error: {e}"


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return 

        if self.bot.user not in message.mentions:
            return

        ctx = await self.bot.get_context(message)
        if ctx.valid:
            return  
        
        if ctx.command:
            return 
        
        prompt = message.content.replace(f"<@{self.bot.user.id}>", "").strip()

        if not prompt:
            return 

        response = await self.get_gemini_response(prompt)
        await message.channel.send(response)

async def setup(bot):
    await bot.add_cog(GeminiChat(bot))
