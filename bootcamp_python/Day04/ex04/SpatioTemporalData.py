import pandas as pd
from FileLoader import FileLoader as loader

class SpatioTemporalData:
	def __init__(self, data):
		self.data = data

	def where(self, year):
		return list(self.data.loc[self.data["Year"] == year]["City"].unique())

	def when(self, location):
		return list(self.data.loc[self.data["City"] == location]["Year"].unique())

def main():
	""" Main program """
	data = loader.load("../ex00/athlete_events.csv")
	data = SpatioTemporalData(data)
	print(data.when("Paris"))
	return 0

if __name__ == "__main__":
	main()
