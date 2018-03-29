# Your Bot Name
BOT_NICKNAME = 'Twitch Bot Account Name'
# Default activation state
TOGGLE = 'ON'
# Your Unix-running Minecraft screen name
SCREEN_NAME = "minecraft"
# Default selector
TELLRAW_SELECTOR = ['@a']
# Display a button to timeout people.
DISPLAY_MOD_BUTTON = True
# Log things in console
logState = True
ChatToggleState = 'ON'
CURRENT_CHANNEL = None
ALLOWED_CHANNELS = ['Channel_1','Channel_2']
mc_log = True
logfilePath = 'minecraft/logs/latest.log' # Your relative or absolute path to the latest log
# Bot Oauth token to connect to IRC chat.
# Get yours : https://twitchapps.com/tmi/
BOT_OAUTH_TOKEN = 'oauth:azertyuiop0123456789azertyuiop'

def get_log_file_path():
    return logfilePath


def get_bot_nickname():
    return BOT_NICKNAME


def get_mc_chat_toggle_state():
    return TOGGLE


def set_mc_chat_toggle_state(string):
    global TOGGLE
    TOGGLE = string


def get_screen_name():
    return SCREEN_NAME


def get_tellraw_selector():
    return TELLRAW_SELECTOR


def set_tellraw_selector(selector_list):
    global TELLRAW_SELECTOR
    TELLRAW_SELECTOR = []
    # Prevent Duplicates
    for item in selector_list:
        if item.lower() not in TELLRAW_SELECTOR:
            TELLRAW_SELECTOR.append(item.lower())


def get_display_mod_button():
    return DISPLAY_MOD_BUTTON


def set_display_mod_button(bolean):
    global DISPLAY_MOD_BUTTON
    DISPLAY_MOD_BUTTON = bolean


def get_log_toggle_state():
    return logState


def get_oauth_token():
    return BOT_OAUTH_TOKEN


def get_chat_toggle_state():
    return ChatToggleState


def set_chat_toggle_state(string):
    global ChatToggleState
    ChatToggleState = string


def get_current_channel():
    return CURRENT_CHANNEL


def set_current_channel(string):
    global CURRENT_CHANNEL
    CURRENT_CHANNEL = string


def get_allowed_channel():
    return ALLOWED_CHANNELS


def get_mc_log_state():
    return mc_log

