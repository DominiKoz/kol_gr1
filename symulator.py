import random
import time

def symulator():
	current_angle = 0
	while 1:
		new_turbulence = random.gauss(0,2)
		print ("Current angle= " + str(current_angle))
		correction = current_angle*(-0.5)
		print ("Correction = " + str(correction)+ "\n")
		current_angle = current_angle - correction + new_turbulence
		time.sleep(2)

symulator()
