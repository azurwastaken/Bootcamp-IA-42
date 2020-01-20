import pandas as pd
from FileLoader import FileLoader as loader

def howManyMedals(df, team):
	data = df.loc[lambda data: data["Team"] == team]
	result = {}
	for year in data["Year"]:
		yearResult = {}
		yearResult['G'] = data.loc[(data["Medal"] == "Gold") & (data["Year"] == year)].shape[0]
		yearResult['S'] = data.loc[(data["Medal"] == "Silver") & (data["Year"] == year)].shape[0]
		yearResult['B'] = data.loc[(data["Medal"] == "Bronze") & (data["Year"] == year)].shape[0]
		result[year] = yearResult
		del yearResult
	return result

def main():
	""" Main program """
	data = loader.load("../ex00/athlete_events.csv")
	print(howManyMedals(data, "Romania"))
	return 0

if __name__ == "__main__":
	main()
