# Disco-AI: Your Discord's New Best Friend! 🎉

Tired of the same old Discord grind? Say hello to Disco-AI, the bot that's here to inject some serious fun and functionality into your server! 🚀 Disco-AI isn't just another bot; it's your personal assistant, conversation starter, and poll master all rolled into one. Imagine having a witty AI at your fingertips, polls that spark lively debates, and reminders that actually keep you on track. Oh, and did we mention it rolls out the red carpet for every new member? Yep, Disco-AI welcomes new users with open arms (or, well, open code)!

## Features

* **🤖 AI Chat: Talk Nerdy to Me!**
    * Dive into hilarious or insightful conversations with our Gemini API-powered AI.
    * Got a massive wall of text? Just ask Disco-AI to `summarize` it, and boom! Instant TL;DR.
    * It's like having a super-smart friend who's always online.
* **📊 Polls: Let the Games Begin!**
    * Create polls that'll have your server buzzing! Up to 10 options? We got you.
    * Set time limits to keep things spicy and get those results rolling in.
    * It's perfect for deciding everything from movie nights to server rule changes.
* **⏰ Reminders: Never Miss a Beat!**
    * Set reminders with our easy-peasy time format and never forget a thing again.
    * Manage your reminders like a pro: list, delete, and modify with simple commands.
    * Disco-AI also cleans up after itself by deleting old reminders.
    * It's like having a digital post-it note ninja!
* **🎉 Welcome Wagon: Party Time!**
    * Disco-AI throws a virtual confetti party for every new member with a customizable welcome message.
    * Make new users feel right at home from the start.

## Commands

### 🤖 AI Chat Commands

* **Mention the bot:** `@Disco-AI <your question>`
    * Example: `@Disco-AI What's the best pizza topping?`
* **Summarize a message:** `@Disco-AI summarize` (as a reply to the message you want to summarize)

### 📊 Poll Commands

* `!poll <question> <option1> <option2> ... [time]`
    * Example: `!poll 'Game Night?' 'Board Games' 'Video Games' 'Card Games' 1d`
    * Time format: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).

### ⏰ Reminder Commands

* `!remindme <time> <message>`
    * Example: `!remindme 2h 'Do the laundry!'`
    * Time format: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).
* `!reminders`
    * List all your active reminders.
* `!delreminder <index>`
    * Delete a reminder by its index.
* `!modifyreminder <index> <new time> <new message>`
    * Modify an existing reminder.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure the Bot:**
    * Create a `.env` file in the root directory of the project.
    * Add your Discord bot token and Gemini API key to the `.env` file. Example:
        ```
        DISCORD_TOKEN=your_discord_bot_token
        GEMINI_API_KEY=your_gemini_api_key
        ```
4.  **Run the Bot:**
    ```bash
    python your_bot_file.py
    ```
    (Replace `your_bot_file.py` with the actual name of your bot's main Python file.)
5.  **Invite the Bot:**
    * Generate an invite link for your bot in the Discord Developer Portal.
    * Use the invite link to add the bot to your Discord server.

## Usage

* Use the commands listed above to interact with the bot.
* Mention the bot to chat with the AI.
* Enjoy the automated welcome message for new users.
