from abc import ABC, abstractmethod
import datetime

class Vehicle(ABC):
	
	def show_registration(self):
		print("You have purchased this at {}".format(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")))
	
	@abstractmethod
	def accelerate(self):
		pass


	def seat_capacity(self):
		pass


class Jeep(Vehicle):

	def __init__(self):
		self.speed = 0
		self._seat_capacity = 8


	def accelerate(self):
		self.speed += 20
		print ("vroom vroom @ {}mph!".format(self.speed))


	def seat_capacity(self):
		print("This vehicle has {} seats available".format(self._seat_capacity))