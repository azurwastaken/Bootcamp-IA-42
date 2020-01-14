import sys
import string

class GotCharacter:
	def __init__(self, first_name, is_alive = True):
		if not isinstance(first_name, str) or len(first_name) == 0:
			raise ValueError("Seems like you fucked up Jackson, put a correct name")
		self.first_name = first_name
		self.is_alive = True

class Stark(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_word(self):
		print(self.house_words)
	
	def die(self):
		self.is_alive = False