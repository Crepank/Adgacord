import discord
import random

TOKEN = 'your_bot_token_here'

client = discord.Client()

egg_locations = {
    'Adga': [(50, 50), (100, 100), (150, 150)]  # Example coordinates for egg locations
}

event_codes = {
    'code1': 'Reward 1',
    'code2': 'Reward 2',
    'code3': 'Reward 3',
    'code4': 'Reward 4',
    'code5': 'Reward 5',
    'code6': 'Reward 6',
    'code7': 'Reward 7',
    'code8': 'Reward 8',
    'code9': 'Reward 9',
    'code10': 'Reward 10',
    'code11': 'Reward 11',
    'code12': 'Reward 12',
    'code13': 'Reward 13',
}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!findegg'):
        server = message.guild.name
        if server in egg_locations:
            egg_location = random.choice(egg_locations[server])
            await message.channel.send(f'An Easter egg has been hidden at coordinates: {egg_location}')
        else:
            await message.channel.send('No Easter egg hidden on this server.')

    if message.content.startswith('!redeem'):
        code = message.content.split()[1]
        if code in event_codes:
            reward = event_codes[code]
            await message.channel.send(f'You have redeemed event code {code}! Your reward is: {reward}')
        else:
            await message.channel.send('Invalid event code.')

client.run(TOKEN)
