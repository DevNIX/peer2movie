import globals


def debug(text):
    if globals.DEBUG:
        print("[" + globals.SERVER_NAME.upper() + "] " + text)
