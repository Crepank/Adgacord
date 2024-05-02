import discord
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

client = discord.Client()

# Function to scrape GitHub repository for hints
def get_hints_from_github(repo_url):
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(repo_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        hint_elements = soup.find_all('span', class_='css-truncate-target')
        hints = [hint.text.strip() for hint in hint_elements]
        return hints
    else:
        return None

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hunt'):
        # Replace with your GitHub repository URL containing hints
        github_repo_url = 'https://github.com/yourusername/yourrepo'
        hints = get_hints_from_github(github_repo_url)
        if hints:
            hint = random.choice(hints)
            await message.channel.send(f'Hint: {hint}')
        else:
            await message.channel.send('Failed to retrieve hints. Check GitHub token or repository URL.')

client.run(TOKEN)
