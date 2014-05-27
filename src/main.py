#! /usr/bin/env python

from storm.locals import *

import Model

print "Loading database"

database = create_database("sqlite:///database/db")
store = Store(database)


"""
padre_de_familia = Model.Show(u"Family Guy")

store.add(padre_de_familia)

store.flush()
store.commit()
"""

all_shows = store.find(Model.Show)

for show in all_shows:
	print "%r, %r" % (show.id, show.original_title)
	show.getGtkModel()