""" This is my Dog class """
from abc import ABC


class Dog:
	
	species = 'Canis Familiaris'

	def __init__(self, name, breed):
		self._name = name
		self._breed = breed

	def breed(self):
		return self._breed
	
	def name(self):
		return self._name

	def speak(self, sound):
		return "{} says {}".format(self._name, sound)

	@staticmethod
	def walk():
		return "This dog is now walking"


class GermanCheckered(Dog):
	def speak(self):
		return "{} says {}".format(self._name, 'Sturgenburdenhardenbardt')


class Siwawa(Dog):
	def speak(self):
		return "{} says {}".format(self._name, 'woof woof')


class NigerianHashkey(Dog):
	def speak(self):
		return "{} says {}".format(self._name, 'bark bark')
