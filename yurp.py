import discord
from discord.ext import commands

# Create a bot instance with a command prefix
intents = discord.Intents.default()
intents.message_content = True  # Ensure the bot can read message content
bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to store counts for each channel
channel_counts = {}

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# Event: When a new message is sent in any channel
@bot.event
async def on_message(message):
    # Avoid bot replying to itself
    if message.author == bot.user:
        return

    # Get the channel ID
    channel_id = message.channel.id

    # Initialize count for the channel if it doesn't exist
    if channel_id not in channel_counts:
        channel_counts[channel_id] = 0

    # Check if the word "nigger" is in the message (case insensitive)
    if 'nigger' in message.content.lower():
        # Increment the counter for the channel
        channel_counts[channel_id] += 1
        # Send a message with the updated count
        await message.channel.send(f"Current nigger Count: {channel_counts[channel_id]}")

    # Process commands if any
    await bot.process_commands(message)

# Run the bot with your token
bot.run('MTM0MDAyMjg4NzM0Nzc4MTY1Mg.Ga1PPO.9lnwfZnch6RnNVqq4DKFI5EksdpZ4AWOfB50mc')
