# Disco-AI Discord Bot

Disco-AI is a versatile Discord bot designed to enhance your server experience with AI-powered chat, polls, and reminders.

## Features

* **🤖 AI Chat:**
    * Respond to user messages in the Discord server using the Gemini API.
    * Summarize long messages using the `summarize` command as a reply.
* **📊 Polls:**
    * Create, polls with up to 10 options.
    * Set optional time limits for polls.
* **⏰ Reminders:**
    * Create, delete, and modify reminders for users.
    * Users set reminders using a specific time and date format.
    * List all active reminders.
    * Delete reminders by index.
    * Modify reminders by index.
    * Auto deletion of expired reminders.
* **🎉 Custom Welcome Messages:**
    * Welcomes new members to the discord server.

## Commands

### 🤖 AI Chat Commands

* **Mention the bot:** `@Disco-AI <your question>`
    * Example: `@Disco-AI How do I use Python?`
* **Summarize a message:** `@Disco-AI summarize` (as a reply to the message you want to summarize)

### 📊 Poll Commands

* `!poll <question> <option1> <option2> ... [time]`
    * Create a poll with a question, options, and an optional time limit.
    * Example: `!poll 'Favorite Band?' AC/DC Metallica Nirvana 1d2h`
    * Time format: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).

### ⏰ Reminder Commands

* `!remindme <time> <message>`
    * Set a reminder with a time and message.
    * Time format: `1y2mo3w4d5h6m7s` (e.g., `1h30m`).
    * Example: `!remindme 1h30m Give clubs quiz`
* `!reminders`
    * List all active reminders.
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
    python bot.py
    ```

5.  **Invite the Bot:**
    * Generate an invite link for your bot in the Discord Developer Portal.
    * Use the invite link to add the bot to your Discord server.

## Usage

* Use the commands listed above to interact with the bot.
* Mention the bot to engage in AI chat.
* The bot will automatically welcome new users.
