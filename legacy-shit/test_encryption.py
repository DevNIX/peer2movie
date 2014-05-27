#! /usr/bin/env python

#from Lib import AES
import boot

#boot.bootstrap()

import threading
import uuid
import sys

from spore import Spore

from encodium import *

# the Field class comes from encodium and allows for nice serialization.
class ChatMessage(Field):

  def fields():
    message = Bytes()
    nick = Bytes()
    uid = Bytes()

# Get the ports as arguments (for easy local testing)
my_port   = int(sys.argv[1])
seed_port = int(sys.argv[2])


if seed_port == 0:                    # This case is for tracker
    me = Spore(seeds=[],
               address=('127.0.0.1', my_port))
elif my_port == 0:                    # A normal client telling the direction to discover
    me = Spore(seeds=[('127.0.0.1', seed_port)],
           address=None)

'''
me = Spore(seeds=[('127.0.0.1', seed_port)],
           address=('127.0.0.1', my_port))
'''

# Global seen, so we don't broadcast messages ad infinitum
seen = {}

@me.handler('chat')
def chat(peer, payload):
  chat_message = ChatMessage.make(payload)
  message = chat_message.message
  nick = chat_message.nick
  uid = chat_message.uid
  if uid not in seen:

    # Mark it as seen
    seen[uid] = True

    # print the message
    print("\n\033[1A" + nick.rjust(10).decode(), ":", message.decode())
    print(nick.rjust(10).decode() + ": ")

    # Relay this message to other peers
    me.broadcast('chat', payload)

# Start it in it's own thread.
threading.Thread(target=me.run).start()

nick = input("What's your nick? ").encode()

print("Type messages to send to the network and press enter.")

try:
  while True:
    message = input(nick.rjust(10).decode() + ": ").encode()
    uid = uuid.uuid4().bytes
    seen[uid] = True
    me.broadcast('chat', ChatMessage.make(message=message, uid=uid, nick=nick))
finally:
  me.shutdown()


"""
crypter = AES("plarg110")
#                     "plarg1107"
#                     "Este es un tex(to de prueba"
print crypter.decrypt(
    "f65d02b71377f05da4e69809c8a6afe47388dcaff37a77d25f8d18\
    baffa0823b92ac670c073c13c5d0653706a735b357f2c957e4aee5\
    11285575ff754b8fc343a1fc2273c267f9b38121788c5f24e748"
)
"""
