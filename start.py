from twitchbot_functions import *
from config import *
import select
import subprocess
import time

if __name__ == '__main__':
    init_bot()
    connectbot()
    logfile = subprocess.Popen(['tail', '-f', '-n', '0', get_log_file_path()],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        newlines = select.poll()
        newlines.register(logfile.stdout)
        try:
            if newlines.poll(1):
                mc_log_interpreter(logfile.stdout.readline())
            for event in get_bot_event():
                twitch_chat_interpreter(event)
        except KeyboardInterrupt:
            exit()
