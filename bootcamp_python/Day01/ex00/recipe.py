class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ""):
		self.name = self.handle_name(name)
		self.cooking_lvl = self.handle_cooklvl(cooking_lvl)
		self.cooking_time = self.handle_cooking_time(cooking_time)
		self.ingredients = self.handle_ingredientlist(ingredients)
		self.description = description
		self.recipe_type = self.handle_recipe_type(recipe_type)
	
	def handle_name(self, name):
		if not isinstance(name,str):
			raise Exception("Name must be a string")
		return name
	
	def handle_cooklvl(self, cooking_lvl):
		if not (isinstance(cooking_lvl, int) and cooking_lvl >= 1 and cooking_lvl <= 5):
			raise Exception("Cooking level must be an int between 1 and 5")
		return cooking_lvl

	def handle_ingredientlist(self, ingredients):
		if not ingredients or len(ingredients) == 0:
			raise Exception("Ingredient list can't be empty")
		while("" in ingredients):
			ingredients.remove("")
		for item in ingredients:
			if not isinstance(item, str):
				raise Exception(f"Look like {item} is not a string")
		return ingredients
	
	def handle_cooking_time(self, cooking_time):
		if not (isinstance(cooking_time, int) and cooking_time > 0):
			raise Exception("Cooking time should be an in greater than 0")
		return cooking_time

	def handle_recipe_type(self, recipe_type):
		if not (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
			raise Exception("Recipe type can only be starter, lunch or dessert")
		return recipe_type
	
	def get_cooking_level(self):
		return self.cooking_lvl

	def get_ingredients(self):
		return self.ingredients
	
	def get_prep_time(self):
		return self.cooking_time

	def get_recipe_type(self):
		return self.recipe_type

	def get_name(self):
		return self.name

	def __str__(self):
		string = [self.get_name]
		string += "About: " + self.get_prep_time() + ".\n"
		string += "Difficulty: " + self.get_cooking_level() + ".\n"
		string += "Perfect for " + self.get_recipe_type() + ".\n"
		string += "ingredients: " + ", ".join(self.get_ingredients()) + ".\n"
		return string