from operator import attrgetter

from point import Point


class Arena(object):
	def __init__(self, width, height):
		self._width = width
		self._height = height

	width = property(attrgetter('_width'))
	height = property(attrgetter('_height'))

	def corner_location(self, id):
		return {0: Point(0, 0),
		        1: Point(0, self.height),
		        2: Point(self.width, self.height),
		        3: Point(self.width, 0)}[id]

