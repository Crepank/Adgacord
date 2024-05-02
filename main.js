const Discord = require('discord.js');
const client = new Discord.Client();
const { token } = require('./config.json'); // Make sure to create a config.json file with your bot token

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', message => {
  if (message.content.toLowerCase() === 'easter egg') {
    message.channel.send('🐣 Happy Easter Egg Hunt! 🐰');
    message.channel.send('Join the hunt! Find all the hidden eggs in our server!');
  }
});

client.login(token);
