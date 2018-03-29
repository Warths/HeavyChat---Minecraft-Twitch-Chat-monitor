## HeavyChat - Minecraft Twitch Chat Monitor

![illustration](https://github.com/Warths/HeavyChat---Minecraft-Twitch-Chat-monitor/raw/master/illustration.png)

HeavyChat is a python script that processes Twitch Message and Minecraft Message.
You can : 

## Features

 - See messages From Twitch in Minecraft
 - Display Subscriber status
 - Timeout Twitch users
 - Perform Twitch commands in Minecraft
 - Change listened  Twitch channel (for servers with multiple streamers)
 - Change Minecraft Players seeing the chat
 - Activate/Deactivate message display

## Requirements

Python 3:
Launch the script `start.py` with Python 3.
TwitchObserver:
This script is made possible with TwitchObserver:
https://github.com/joshuaskelly/twitch-observer
#### Installation 

    $ pip install twitchobserver

## Commands
### Minecraft Commands :
Activating the chat displaying:

    !heavychat toggle

Changing the current channel:

    !heavychat switch <Target>
Will only work if the channel is in `config.py` ALLOWED_CHANNELS variable.
Exemple : 

    !heavychat switch Warths
 
 Changing message display target:

     !heavychat selector <arg1> <arg2> <arg3>
at least 1 argument required. Compatible with @a.
Exemples :

    !heavychat selector @a
    !heavychat selector Warths Hisokanen TooManyRedirect

Unbanning twitch username:

    !heavychat unban <username>
Exemple : 

    !heavychat unban ValentinDeville
Timeout twitch username

    !heavychat timeout <username>
Compatible with Twitch timeout arguments
Exemple : 

    !heavychat timeout Hisokanen 1
    !heavychat timeout Kyriog
    !heavychat timeout ValentinDeville 3600 Insults
Displaying Help Panel:

    !heavychat help

### Twitch Commands

You can type all Minecraft Commands in twitch chat.

### Configuration:
You have to change some Variables in `config.py` to make the bot work for you.

```python
BOT_NICKNAME = 'your_bot_name' # Your bot twitch username (lowercase)
SCREEN_NAME = "minecraft" # Screen name
TELLRAW_SELECTOR = ['@a']  # Default tellraw selector at startup
DISPLAY_MOD_BUTTON = True # If you want to deactivate the mod button
ALLOWED_CHANNELS = ['channel_1', 'channel_2', 'channel_3']  
logfilePath = '_FILL THIS WITH YOUR MINECRAFT REALTIME LOG PATH_'
BOT_OAUTH_TOKEN = 'oauth:azertyuiop0123456789azertyuiop'
```

You can get you OAUTH token here : https://twitchapps.com/tmi/


