from operator import attrgetter

from point import Point


class Arena(object):
	def __init__(self, width, height):
		self._width = width
		self._height = height

	width = property(attrgetter('_width'))
	height = property(attrgetter('_height'))

	def corner_location(self, id):
		x = self._width * int(id / 2)
		y = self._height * ( id == 1 or id == 2 )
		return Point(x, y)
