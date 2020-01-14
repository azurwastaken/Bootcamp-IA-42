import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		if len(name) == 0:
			raise Exception("Book need name")
		self.name = name
		self.creation_date = datetime.datetime.now()
		self.last_update = datetime.datetime.now()
		self.recipe_list = {
			"starter" : [],
			"lunch" : [],
			"dessert" : [],
		}
	
	def is_recipe_exist(self, name):
		if name in self.recipe_list["starter"]:
			raise Exception("recipe already exist in starter list")
		if name in self.recipe_list["lunch"]:
			raise Exception("recipe already exist in lunch list")
		if name in self.recipe_list["dessert"]:
			raise Exception("recipe already exist in dessert list")


	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for item in self.recipe_list["starter"]:
			if item.get_name() == name:
				print(item)
				return
		for item in self.recipe_list["lunch"]:
			if item.get_name() == name:
				print(item)
				return
		for item in self.recipe_list["dessert"]:
			if item.get_name() == name:
				print(item)
				return 

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for item in self.recipe_list[recipe_type]:
			print(item.get_name())

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if not isinstance(recipe, Recipe):
			raise Exception("recipe is not an instance of Recipe")
		self.recipe_list[recipe.get_recipe_type()].append(recipe)
		self.last_update = datetime.datetime.now()  
		
