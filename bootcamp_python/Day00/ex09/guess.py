import random
import sys

def handle_win(result, tryamount):
	if result == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	print("Congratulations, you've got it",end = "")
	if tryamount == 1:
		print("on your first try!")
	else:
		print(f"!\nYou won in {tryamount} attempts")

def main():
	print(
		"This is an interactive guessing game!"
		"You have to enter a number between 1 and 99 to find out the secret number."
		"Type 'exit' to end the game."
		"Good luck!"
	)
	tryamount = 0
	result = random.randint(1,99)
	answer = -1
	while answer != result:
		answer = input("What's your guess between 1 and 99?\n>> ")
		if not answer.isnumeric():
			print("That's not a number.")
		else:
			tryamount += 1
			answer = int(answer)
			if answer == result:
				handle_win(result, tryamount)
				return
			elif answer > result:
				print("Too High !")
			elif answer < result:
				print("Too Low !")

	


if __name__ == "__main__":
	main()