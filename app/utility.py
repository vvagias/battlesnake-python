import json
import math

def distanceBetweenTwoPoints(point1, point2):
	return math.sqrt( (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 )