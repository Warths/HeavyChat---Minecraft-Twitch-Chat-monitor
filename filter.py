import re

MAX_MESSAGE_LENGHT = 240
BAD_WORDS = ['caca']


def spam_filter(message):
    result = 0
    result += long_message(message)
    result += url_filter(message)
    result += me_filter(message)
    return result  # Return how many filter the message triggered


def long_message(message):
    if len(message) > MAX_MESSAGE_LENGHT:
        return 1
    return 0


def url_filter(message):
    if re.match('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', message):
        return 1
    return 0


def me_filter(message):
    #if re.match('([\W][A][C][T][I][O][N])', message):
    #    return 1
    return 0
