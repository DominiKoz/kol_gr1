#!/usr/bin/env python2.7

import random


class Airplane(object):

	def __init__(self):
		self.current_angle = random.gauss(0,3)
		self.correction = 0

	def calculate_correction(self, angle):
		return angle * (-0.6)

	def add_turbulence(self):
		self.current_angle += random.gauss(0,3)

	def correct_position(self):
		self.correction = self.calculate_correction(self.current_angle)
		self.current_angle += self.correction


