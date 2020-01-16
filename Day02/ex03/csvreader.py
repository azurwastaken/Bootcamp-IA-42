import csv


class CsvReader():
	def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		self.file = open(self.filename, "r")
		self.lines = self.file.readlines()
		if (self.skip_top + self.skip_bottom) > len(self.lines):
			raise ValueError("Seems like you don't want to read any line of your file ^^")
		self.data = self.getdata()
		if self.data == None:
			return None
		return self

	def __exit__(self, type, value, traceback):
		self.file.close()

	def getdata(self):
		header = self.getheader()
		first_data_line = self.skip_top
		if not self.header:
			first_data_line += 1
		last_data_line = len(self.lines) - self.skip_bottom
		amount_of_data_by_line = len(self.lines[first_data_line].split(self.sep))
		
		data = []
		for line in self.lines:
			line = line.split(self.sep)
			if len(line) > amount_of_data_by_line:
				return None
			for i,field in enumerate(line):
				field = field.replace("\"", "")
				field = field.replace("\'", "")
				line[i] = field.strip()
			data.append(dict(zip(header,line)))
		return data[:last_data_line]

	def getheader(self):
		header = self.lines[0] if self.header else self.lines[self.skip_top]
		header = header.split(self.sep)
		for i,field in enumerate(header):
				field = field.replace("\"", "")
				field = field.replace("\'", "")
				header[i] = field.strip()
		return header