#!/usr/bin/env python2.7

import time
from airplane import Airplane

class Symulator(object):
	def __init__(self):
		self.airplane = Airplane()

	def start(self):
		while True:
			self.airplane.add_turbulence()
			print "angle after turbulence: %.3f" % self.airplane.current_angle
			self.airplane.correct_position()
			print "correction made: %.3f" % self.airplane.correction
			print "new angle: %.3f \n" % self.airplane.current_angle
			time.sleep(2)

if __name__ == "__main__":
	symulator = Symulator()
	symulator.start()
