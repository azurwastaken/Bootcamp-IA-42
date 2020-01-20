import pandas as pd
from FileLoader import FileLoader as loader

def ProportionBySport(df, year, sport, gender):
	data = df.loc[lambda data: data["Year"] == int(year)]
	data = data.loc[lambda data: data["Sex"] == gender]
	data = data.drop_duplicates(subset="Name")
	result = data.shape[0]	
	data = data.loc[lambda data: data["Sport"] == sport]
	result = data.shape[0] / result
	return result

def main():
	""" Main program """
	data = loader.load("../ex00/athlete_events.csv")
	print(ProportionBySport(data, 2004,"Tennis", 'F'))
	return 0

if __name__ == "__main__":
	main()
