# Telegram Cleaner Bot

This is a Telegram bot built with Python that automatically deletes join and left messages from a Telegram group.

## Features

- Deletes messages when users join the group.
- Deletes messages when users leave the group.

## Prerequisites

- Python 3.7 or higher
- A Telegram bot token (You mentioned you already have one)

## Setup

1. Clone this repository or download the files.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Telegram bot token as an environment variable:

On Linux/macOS:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

On Windows (cmd):
```cmd
set TELEGRAM_BOT_TOKEN=your_bot_token_here
```

4. Run the bot:

```bash
python main.py
```

## Deployment

### GitHub

1. Initialize a git repository and commit your code:

```bash
git init
git add .
git commit -m "Initial commit"
```

2. Create a new repository on GitHub and push your code:

```bash
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin master
```

### Railway

1. Create a new project on [Railway](https://railway.app/).

2. Connect your GitHub repository to Railway.

3. Set the environment variable `TELEGRAM_BOT_TOKEN` in Railway project settings.

4. Deploy the project.

## Notes

- Make sure your bot is added to the Telegram group and has admin rights to delete messages.

- The bot uses polling to receive updates.

## License

MIT
