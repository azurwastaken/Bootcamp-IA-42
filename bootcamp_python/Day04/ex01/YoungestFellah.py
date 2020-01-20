import pandas as pd
from FileLoader import FileLoader as loader

def youngestFellah(df, year):
	data = df.loc[lambda data: data["Year"] == int(year)]
	male = data.loc[lambda data: data["Sex"] == "M"]	
	female = data.loc[lambda data: data["Year"] == "F"]
	result = {"m" : male.min()["Age"], "f": female.min()["Age"]}
	return result

def main():
	""" Main program """
	data = loader.load("../ex00/athlete_events.csv")
	print(youngestFellah(data, 2013))
	return 0

if __name__ == "__main__":
	main()
