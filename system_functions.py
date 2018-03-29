from config import *
import subprocess


def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        print('Echec de la commande : ' + cmd)
        return


def mc_cmd(string):
    if len(string) > 600:
        # We're cutting the string into multiple pieces if it's to long to be processed by the subprocess module.
        length = 600
        chunks = [string[i:i + length] for i in range(0, len(string), length)]
        # Sending multiple string pieces in the corresponding screen
        for chunk in chunks:
            # Escaping charaters after spliting to avoid conflicts with Bash syntax.
            chunk = chunk.replace('"', '\\"')
            run_cmd('screen -S %s -X stuff "%s"' % (get_screen_name(), chunk))
        # Sending a "Return" character in the screen to send the command to Minecraft.
        run_cmd('screen -S %s -X stuff "^M"' % get_screen_name())
    else:
        # If the command is short enought to be processed by a single run_cmd(), the characher "Return"
        # is included to avoid going multiple times in the screen. Faster.
        string = string.replace('"', '\\"')
        run_cmd('screen -S %s -X stuff "%s^M"' % (get_screen_name(), string))
