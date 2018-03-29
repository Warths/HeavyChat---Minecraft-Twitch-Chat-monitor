# Module: twitchbot_functions.py
from twitchobserver import *
from system_functions import *
from filter import *
import random
import re

def init_bot():
    global observer
    observer = Observer(get_bot_nickname(), get_oauth_token())
    observer.start()
    log('Initialisation du Bot', True)


def tellraw(message, username=None, subscriber=None):
    if username:
        # If the spam filter detects something wrong, it will stop here.
        if spam_filter(message):
            return
        # Send the message into a subroutine that will change its content to avoid unintended content.
        message = tellraw_message_reformat(message, username)
        # Starting to construct our tellraw string.
        tellrawstr = '['
        # Adding a mod button if get_display_mod_button return true
        if get_display_mod_button():
            tellrawstr += '"",{"text":"✖","clickEvent":{"action":"run_command","value":"!heavychat timeout %s"},' \
                       '"hoverEvent":{"action":"show_text","value":"Expulser %s 600 secondes"}},' % (username, username)
        # Adding Subscriber string.
        if 'subscriber/0' in subscriber:
            tellrawstr += '{"text":" "},{"text":"Sub","color":"gold"},{"text":"","bold":true,"color":"white"},'
        elif 'subscriber/3' in subscriber:
            tellrawstr += '{"text":" "},{"text":"SUB","color":"gold"},{"text":"","bold":true,"color":"white"},'
        elif 'subscriber/6' in subscriber:
            tellrawstr += '{"text":" "},{"text":"SUB","color":"yellow"},{"text":"","bold":true,"color":"white"},'
        elif 'subscriber/12' in subscriber:
            tellrawstr += '{"text":" "},{"text":"SUB","color":"aqua"},{"text":"","bold":true,"color":"white"},'
        elif 'subscriber/24' in subscriber:
            # 24 month subscribers are specials, so is the tellraw formating.
            # Too long to be processed by a single subprocess bash
            # It will be fragmented them sent in multiple pieces. Seems reliable.
            tellrawstr += '{"text":" "},{"text":"O","bold":true,"obfuscated":true,"color":"gray"},' \
                          '{"text":"SUB","bold":true,"color":"aqua"},' \
                          '{"text":"O","bold":true,"obfuscated":true,"color":"gray"},' \
                          '{"text":"","bold":true,"color":"white"},'
        # Adding nickname and message
        tellrawstr += '{"text":" "},{"text":"%s","color":"dark_purple"},{"text":": %s"}]' % (username, message)
    else:
        # If username wasn't specified, will sent a classic tellraw log command.
        tellrawstr = '["",{"text":"["},{"text":"HeavyChat","color":"dark_red"},{"text":"] ▶▶ %s"}]' % message
    print(message)
    send_tellraw(tellrawstr)


def send_tellraw(tellraw_args):
    # Checking if @a is present in selectors.
    # We don't want to send to all selectors if @a is present, or we will have duplicates.
    if '@a' in get_tellraw_selector():
        selector_list = ['@a']
    else:
        selector_list = get_tellraw_selector()
    # Selector list was made either ['@a'] or all other selectors.
    # Looping to send the tellraw to each selector
    for Selector in selector_list:
        tellraw_command = 'tellraw %s %s' % (Selector, tellraw_args)
        mc_cmd(tellraw_command)



def tellraw_message_reformat(string, username):
    # Remplace les guillemets par des doubles apostrophes, pour éviter les problèmes de caractères échapés
    string = string.replace('"', "''")
    # Will replace fake donations by stupid messages.
    if 'has donated' in string or 'has donate' in string or 'ACTION donate' in string:
        gogole_string = ["Ma maman va me disputer si elle sait que je ne suis pas au lit.",
                         "Mon papa et ma maman, ils sont frère et soeur, c'est normal ?",
                         "J'essaie d'être intelligent. C'est vraiment dur...",
                         "Ca vient quand la puberté ? Je complexe, ca doit venir avant 15 ans non ?",
                         "Je te souhaite le meilleur.",
                         "Ma maman dit que je ne devrais pas sucer mon pouce à cet âge.",
                         "J'ai raté mon brevet, car ma passion c'est spammer sur les tchats. Je suis tellement seul.",
                         "%s, tu es mon idéal masculin.. J'dis pas que j'aime les hommes, mais tu me fais de l'effet."
                         % get_current_channel(),
                         "J'ai toujours admiré %s en secret.. J'ai son poster dans ma chambre." % get_current_channel(),
                         "Ma passion ne se résume qu'à une seule chose : me nourrir des produits de mon corps !",
                         "Être avec vous me fait ressentir un profond manque de confiance en moi.. " 
                         "Vous êtes tous tellement intelligents !",
                         "Pour la Nasa, l'espace est une priorité. Ils veulent m'y envoyer..",
                         "J'adore mettre des cornichons dans mon nez, ça donne du gouts à ce que je mange.",
                         "Mon légume préféré, c'est l'aubergine ! Pourquoi ? On a tous droit à nos petits secrets.. ;)",
                         "Ma maman m'a dit que z'étais SHPECHIAL.",
                         "%s !! ..J'apprécie les fruits, en sirop." % get_current_channel().upper(),
                         "La différence fondamentale entre une brique et moi, c'est que je m'appelle %s" % username,
                         "Comment vous faites vos lacets ? Je trouve ca vraiment très compliqué ..",
                         "Ce truc sous mon nombril, vous croyez que c'est une excroissance graisseuse ?",
                         "Mon test de QI sur internet affiche %s ! Ca fait combien ? J'ai pas assez de doigts."
                         % random.randint(70, 90),
                         "Si vous avez des problèmes pour vous intégrer en société.. Vous n'êtes pas seuls.",
                         "J'ai des poils qui poussent un peu partout, je deviens grand !",
                         "Au moins, sur internet, quand je me comporte bêtement, personne ne sait qui je suis.",
                         "Quelle vie on mène, tout de même, quand on a 47 chromosomes !"]
        twitch_message('/timeout %s 36000' % username)
        integer = random.randint(0, len(gogole_string)-1)
        string = gogole_string[integer]
    # Evite l'ajout d'arguments de formatage, de caractères échappés, et l'utilisation du /me.
    for RegexRules in ['([§]+[a-zA-Z1-9§]?)',
                       '([\W][A][C][T][I][O][N])',
                       '([{}[\]])']:
        string = re.sub(RegexRules, '', string)
    return string


def mc_log_interpreter(logline):
    regexrule = "(b'\[[\d][\d]:[\d][\d]:[\d][\d]] \[Server thread/INFO]: <)"
    logline = str(logline)
    if re.match(regexrule, logline):
        logline = re.sub("(b'\[[\d][\d]:[\d][\d]:[\d][\d]] \[Server thread/INFO]: <)", '', str(logline))
        message = logline.split('> ', 1)[1]
        message = message.replace("\\n'", '')
        print(message)
        if "!heavychat" in message.lower() and '!' in message[0]:
            command(message)
    else:
        print(logline)
        print("Log Line not matching, skiping.")


def twitch_chat_interpreter(event):
    # We only want to parse messages from users and ignore system messages, that don't have tags.
    if event.type == 'TWITCHCHATMESSAGE' and hasattr(event, 'tags'):
        # Only Allowed channel can manipulate the bot.
        if event.tags['display-name'].lower() in get_allowed_channel():
            # Only sending !heavychat commands
            if '!heavychat' in event.message.lower():
                command(event.message.lower())
        # Relay twitch Chat in minecraft
        if get_mc_chat_toggle_state() == 'ON':
            tellraw(event.message, event.tags['display-name'], event.tags['badges'])


def command(string):
    parsed_command = command_parse(string)
    # Commands with their minimum numbers of arguments, including command prefix
    # Commands "!heavychat toggle" switch ON/OFF ingame Twitch Chat
    if '!heavychat toggle' in string:
        mc_chat_toggle()
    # Command "!heavychat switch ChannelName" switch to channel.
    # Does nothing if the channel is not in config "Allowed channels"
    elif '!heavychat switch' in string and len(parsed_command) == 3:
        connectbot(parsed_command[2])
    # Change the tellraw selector. If @a is in the selectors, will only target @a
    # USAGE :
    # !heavychat selector set arg1 arg2 arg3 (overwrite previous selectors by those specified)
    # !heavychat selector add arg1 arg2 arg3 (add new selectors, avoids duplicates)
    # !heavychat selector remove arg1 arg2 arg3 (remove selectors, skip if not present)
    elif '!heavychat selector' in string:
        heavychat_selector(parsed_command)
    # Quick Twitch Command. Unban the target.
    # Usage :
    # !heavychat unban <target>
    elif '!heavychat unban' in string and len(parsed_command) == 3:
        twitch_message('/unban %s' % parsed_command[2])
    # Quick Twitch Command. Unban the target.
    # Usage :
    # !heavychat timeout <target> <duration(optionnal)> <reason(optionnal)>
    elif '!heavychat timeout' in string and len(parsed_command) >= 3:
        tostring = ''
        for item in parsed_command[2:]:
            tostring += item
        twitch_message('/timeout %s' % tostring)
    elif '!heavychat help' in string:
        usage_help()


def usage_help():
    heavychat_help = ["Guide d'utilisation d'HeavyChat",
                      "Canal Twitch actuel %s" % get_current_channel(),
                      "=== Commandes ====",
                      "Activer/Désactiver HeavyChat",
                      "!heavychat Toggle",
                      "Switcher le bot sur un autre canal autorisé",
                      "!heavychat switch <arg1>",
                      "Modifier les destinataires d'HeavyChat",
                      "!heavychat selector [set|add|remove] <arg1> <arg2>",
                      "Commandes Twitch rapides",
                      "!heavychat [/unban|/timeout] <arg1> <arg2>"]
    for line in heavychat_help:
        tellraw(line)


def heavychat_selector(parsed_command):
    # To set, add or remove a list of Minecraft Account that will see messages.
    selector_change_type = parsed_command[2]
    if len(parsed_command) >= 4:
        args_list = parsed_command[3:]
    else:
        tellraw('Arguments manquants. Utilisation : !heavychat selector set|add|remove arg1 arg2')
        return
    # Set new selector using the setter.
    if 'set' in selector_change_type:
        current_selector_list = args_list
    # Add take the current list, add new content then set it.
    elif 'add' in selector_change_type:
        current_selector_list = get_tellraw_selector()
        for Argument in args_list:
            current_selector_list.append(Argument)
    # Remove take the current list and try to remove matching selectors.
    elif 'remove' in selector_change_type:
        current_selector_list = get_tellraw_selector()
        for Argument in args_list:
            if Argument in current_selector_list:
                current_selector_list.remove(Argument)
    # Return a usage message if none of the selector type matched.
    else:
        tellraw('Type de changement de selecteur invalide. Utilisation : !heavychat selector set|add|remove arg1 arg2')
        return
    set_tellraw_selector(current_selector_list)
    tellraw("Nouveaux selecteurs : %s" % get_tellraw_selector())


def command_parse(command):

    parsed_command = command.split()
    if '!' in parsed_command[0][0]:
        return parsed_command
    else:
        return ['Invalid']


def log(string, inminecraftchat=False):
    if get_log_toggle_state():
        print(string)
    if inminecraftchat:
        tellraw(string)


def mc_chat_toggle():
    if get_mc_chat_toggle_state() == 'OFF':
        set_mc_chat_toggle_state('ON')
        log('Nouveau réglage défini : ChatToggleState = ON', True)
    else:
        set_mc_chat_toggle_state('OFF')
        log('Nouveau réglage défini : ChatToggleState = OFF', True)


def connectbot(channel_name=get_allowed_channel()[0]):
    if channel_name in get_allowed_channel():
        if get_current_channel() is not None:
            log('Déconnection du canal Twitch : %s' % get_current_channel(), True)
            observer.leave_channel(get_current_channel())
        observer.join_channel(channel_name)
        set_current_channel(channel_name)
        log('Connection au canal Twitch : %s' % channel_name, True)
    else:
        log('Connection échouée au canal Twitch : %s (Canal non-autorisé). Connection au canal %s maintenue'
            % (channel_name, get_current_channel()), True)


def get_bot_event():
    return observer.get_events()


def twitch_message(string):
    observer.send_message(string, get_current_channel())
    log('Twitch Message function called : %s ' % string)


