import random
import sys
import os

class Cookbook:
	def __init__(self, cookbook):
		self.cookbook = cookbook
	
	def print_recipelist(self):
		for recipe in self.cookbook:
			print(recipe)

	def print_recipe(self, name):
		if name in self.cookbook:
			print(f"[{name}]\n\n{self.cookbook[name]}")
		else:
			print(f"There is no recipe called {name} in this cookbook")

	def delete_recipe(self, name):
		try :
			del(self.cookbook[name])
		except:
			print(f"There is no recipe called {name} in this cookbook")
	
	def add_recipe(self, name, ingredients, meal, prep_time):
		if name in self.cookbook:
			print(f"There is already a recipe called {name} in this cookbook\n")
		new_recipe = Recipe(ingredients, meal, prep_time)
		self.cookbook[name] = new_recipe

class Recipe:
	def __init__(self,ingredients, meal, prep_time):
		self.ingredients = ingredients
		self.meal = meal
		self.prep_time = prep_time

	def get_ingredients(self):
		return(self.ingredients)

	def get_meal(self):
		return(self.meal)

	def get_preptime(self):
		return(str(self.prep_time))

	def __str__(self):
		string = "ingredients: " + ", ".join(self.get_ingredients()) + ".\n"
		string += "meal: " + self.get_meal() + ".\n"
		string += "prep_time: " + self.get_preptime() + ".\n"
		return string


class Dictionnary_utils:
	def print_keys(self, dictionnary):
		for elem in dictionnary:
			print(elem)

	def print_elements(self, dictionnary):
		for elem in dictionnary:
			print(dictionnary[elem])
	
	def print_dictionnary(self, dictionnary):
		for elem in dictionnary:
			print(f"[{elem}] : {dictionnary[elem]}")

class Menu:
	def __init__(self, cookbook):
		self.cookbook = cookbook
		self.welcome_message = "Welcome to mcaseaux's cookbook\nPlease select an option by typing the corresponding number:"
		self.mainmenu = ["What do you want to do next ?", "How can I help you ?", "Can I do something more for you ?"]
		self.options = {
			'1' : 'Add a recipe',
			'2' : 'Delete a recipe',
			'3' : 'Print a recipe',
			'4' : 'Print the cookbook',
			'5' : 'Quit',
		}

	def handle_add_recipe(self):
		name = input("Ok, let's add a new recipe ! first of all, what's his name ?\n")
		if name in self.cookbook.cookbook:
			name = input("Oups there is already one recipe with this name, try another one\n")
		meal = input("When should we eat this ?\n")
		prep_time = input("how much time is needed to do it ? Type it in minutes\n")
		ingredient_list = []
		while not prep_time.isnumeric():
			prep_time = input("It's look like you miss typed, make sure to enter a full amount of minutes\n")
		ingredient = input("Now let me know what should I buy, hit enter after each ingredient, hit it twice once finished\n")
		while len(ingredient) > 0:
			ingredient_list.append(ingredient)
			ingredient = input()
		self.cookbook.add_recipe(name, ingredient_list, meal, prep_time)
	
	def handle_delete_recipe(self):
		name = input("Which recipe should I delete for you ?\n")
		self.cookbook.delete_recipe(name)

	def handle_print_recipe(self):
		name = input("Alright ! Which recipe should I print for you ?\n")
		self.cookbook.print_recipe(name)

	def handle_printall(self):
		print("Here is the list of all the recipes :\n")
		self.cookbook.print_recipelist()

	def welcome(self):
		os.system('clear')
		print(self.welcome_message)

	def anykey(self):
		print("Press Enter to continue")
		input()
		self.main()

	def select_option(self):
		print("\n")		
		for i in self.options:
			print(f"{i}: {self.options[i]}")
		choice = input("\n>>> ")
		print("\n")
		if choice == "1":
			self.handle_add_recipe()
		elif choice == "2":
			self.handle_delete_recipe()
		elif choice == "3":
			self.handle_print_recipe()
		elif choice == "4":
			self.handle_printall()
		elif choice == "5":
			print("Hope you enjoyed, see you later ! :)")
			return
		else:
			print("Invalid choice, please try again")
		self.anykey()
		
	def main(self):
		os.system('clear')
		print(random.choice(self.mainmenu))
		self.select_option()

		

def main():
	cookbook = Cookbook({
		'sandwich' : Recipe(["ham", "bread", "cheese", "tomatoes"], "lunch", 10),
		'cake' : Recipe(["flour", "sugar", "eggs"], "desert", 60),
		'salad' : Recipe(["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15),
	})
	menu = Menu(cookbook)
	menu.welcome()
	menu.select_option()


if __name__ == "__main__":
	main()