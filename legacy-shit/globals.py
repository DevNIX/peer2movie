import sys

# Debug mode
global DEBUG
DEBUG = True

# Config folder
global CONFIG_FOLDER
CONFIG_FOLDER = "config"

# Server name
global SERVER_NAME

try:
    SERVER_NAME = sys.argv[1]
except IndexError:
    SERVER_NAME = "default"

# Time for attemping a new connection to a tracker (in seconds)
global RECONNECT
RECONNECT = 2
