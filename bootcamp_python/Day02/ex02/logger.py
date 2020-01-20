import time
import getpass
from random import randint

def log(func):
	def timed(*args, **kw):
		ts = time.time()
		result = func(*args, **kw)
		te = time.time()
		timer = (te - ts)
		if timer > 0.5:
			timer = ('%.4f s' % ((te - ts)))
		else:
			timer = ('%.4f ms' % ((te - ts) * 1000))
		name = func.__name__
		name = name.replace('_', ' ').title()	
		f= open("machine.log","a+")
		f.write(f"({getpass.getuser()})Running: {name.ljust(20)}[ exec-time = {timer} ]\n")
		return result

	return timed

class CoffeeMachine():
	water_level = 100
	@log
	def start_machine(self):
	 if self.water_level > 20:
		 return True
	 else:
		 print("Please add water!")
		 return False
	@log
	def boil_water(self):
		return "boiling..."
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)