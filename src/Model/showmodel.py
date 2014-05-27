from storm.locals import *
from Class.Model import GtkAdapter


class Show(GtkAdapter):
	__storm_table__ = "shows"

	id = Int(primary = True)
	network_id = RawStr()
	original_title = Unicode()
	year_started = Int()
	minutes_per_chapter = Int()

	def __init__(self, title):
		self.original_title = title