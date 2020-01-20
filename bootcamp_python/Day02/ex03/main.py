from csvreader import CsvReader

def main():
	with CsvReader('bad.csv') as file:
		if file == None:
			print("File is corrupted")

if __name__ == "__main__":
	main()