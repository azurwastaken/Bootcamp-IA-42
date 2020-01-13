import sys
import datetime

def main():
	date = (3,30,2019,9,25)
	date = datetime.datetime(date[2], date[3], date[4], date[0], date[1])
	date = date.strftime("%m/%d/%Y %H:%M")
	print(date)


if __name__ == "__main__":
	main()