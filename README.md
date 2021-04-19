# Tamil Voicechat UserBot

A Telegram UserBot to Play music 🎶 in Voice Chats.

It's recommended to use an USA number.(if your real number is suspended I'm not responsible.use at your own risks) no grauanty no waranty
Use at your own risks..

## Give your 💙

Before clicking on deploy to heroku just click on fork and star just below

<p align="center">
  <a href="https://github.com/tamilbots/tamilvcbot/fork">
    <img src="https://img.shields.io/github/forks/tamilbots/tamilvcbot?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/tamilbots/tamilvcbot">
    <img src="https://img.shields.io/github/stars/tamilbots/tamilvcbot?style=social">
  </a>
</p>

## How to deploy 

Click the below button to watch the video tutorial on deploying

<a href="https://youtu.be/ThJQYQLcSsg"><img src="https://img.shields.io/badge/How%20To%20Deploy-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/ThJQYQLcSsg"><img src="https://img.shields.io/youtube/views/ThJQYQLcSsg?style=social">

###  GET STRING SESSION FROM REPL RUN

 [![Run on Repl.it](https://camo.githubusercontent.com/05149b448485553c6f14f6430a45c12dcc79ed3c/68747470733a2f2f7265706c2e69742f62616467652f6769746875622f6a61727669733231303930342f4a6172766973)](https://replit.com/@TamilBots/generate-pyrogram-session-string#main.py)

<b> Deploy to Heroku </b>
[![tamilbot logo](https://telegra.ph/file/6babc0f95a5362fd27872.jpg)](https://heroku.com/deploy?template=https://github.com/TamilBots/TamilVcBot)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TAMILBOTS/TAMILVCBOT)

- Enable the worker after deploy the project to Heroku
- send `!ping`, `!uptime`, or `!sysinfo` from userbot account itself or its contacts to check if the userbot is running or not.
- Send `!join` to a voice chat enabled group chat from userbot account itself or its contacts.

**Features**

- Playlist, queue
- Loop one track when there is only one track in the playlist
- Automatically downloads audio for the first two tracks in the playlist
  to ensure smooth playing
- Automatically pin the current playing track
- Show current playing position of the audio

**How to Use the Player plugin**

1. Start the userbot
2. send `!join` to a voice chat enabled group chat from userbot account itself
   or its contacts, be sure to make the userbot account as group admin and
   give it at least the following permissions:
   - Delete messages
   - Manage voice chats (optional)
3. reply to an audio with `/play` to start playing it in the voice chat, every
   member of the group can use common commands such like `/play`, `/current` and `!help` now.
4. check `!help` for more commands

**Commands**

The main plugin is `vc.player` which has the following command commands and admin commands.
After start the bot, send `!join` to a voice chat enabeld group chat from userbot account
itself or its contacts, and then common commands like `/play` and `/current` will be available
to every member of the group. send `!help` to check more commands.

- Common commands, available to group members of current voice chat
- starts with / (slash) or ! (exclamation mark)

| Common Commands | Description                                            |
|-----------------|--------------------------------------------------------|
| /play           | reply with an audio to play/queue it, or show playlist |
| /current        | show current playing time of current track             |
| /repo           | show git repository of the userbot                     |
| !help           | show help for commands                                 |

- Admin commands, available to userbot account itself and its contacts
- starts with ! (exclamation mark)

| Admin Commands | Description                      |
|----------------|----------------------------------|
| !skip [n] ...  | skip current Song!               |
| !join          | join voice chat of current group |
| !leave         | leave current voice chat         |
| !vc            | check which VC is joined         |
| !stop          | stop playing                     |
| !replay        | play from the beginning          |
| !clean         | remove unused RAW PCM files      |
| !pause         | pause playing                    |
| !resume        | resume playing                   |
| !mute          | mute the VC userbot              |
| !unmute        | unmute the VC userbot            |

- Commands from other plugins, available only to userbot account itself

| Plugin  | Commands | Description         |
|---------|----------|---------------------|
| ping    | !ping    | show ping time      |
| uptime  | !uptime  | show userbot uptime |
| sysinfo | !sysinfo | show system info    |

## Requirements

- Python 3.6 or higher
- A [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api) and a Telegram account
- Choose plugins you need, install dependencies which listed above and run `pip install -U -r requirements.txt` to install python package dependencies as well
- [FFmpeg](https://www.ffmpeg.org/)

## Run

Choose one of the two methods and run the userbot with
`python userbot.py`, stop with <kbd>CTRL+c</kbd>. The following example
assume that you were going to use `vc.player` and `ping` plugin, replace
`api_id`, `api_hash` to your own value.

# Credits :

This Repo Is Just A Custom Fork Of [callsmusic/tgvc-userbot](https://github.com/callsmusic/tgvc-userbot)
