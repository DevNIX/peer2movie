#! /usr/bin/env python3

from gi.repository import Gtk


def loginWindow():
    builder = Gtk.Builder()
    builder.add_from_file("interface/login.glade")

    loginWindow = builder.get_object("loginWindow")
    loginWindow.show_all()

    def login(data):
        loginWindow.hide()
        chatWindow()

    events = {
        "login": login,
        "close": Gtk.main_quit
    }

    builder.connect_signals(events)


def chatWindow():
    builder = Gtk.Builder()
    builder.add_from_file("interface/chat.glade")

    chatWindow = builder.get_object("chatWindow")
    chatWindow.show_all()

    events = {
        "close": Gtk.main_quit
    }

    builder.connect_signals(events)


def main():
    #loginWindow()
    chatWindow()
    Gtk.main()

if __name__ == "__main__":
    main()
