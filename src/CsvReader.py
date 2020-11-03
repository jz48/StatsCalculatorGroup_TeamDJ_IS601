import csv


class CsvReader:
	data = []

	def __init__(self, filepath):
		# print('filepath', filepath)
		# a bug is detected here, data need to be cleared each time running a reader, if not, all the data would
		# accumulate together and the error would occur.
		self.data = []
		with open(filepath) as text_data:
			csv_data = csv.DictReader(text_data)
			for row in csv_data:
				# print('row: ', row)
				self.data.append(row)
		pass

	def return_data_as_objects(self, class_name):
		objects = []
		for row in self.data:
			objects.append(ClassFactory(class_name, row))
		return objects


def ClassFactory(class_name, dictionary):
	return type(class_name, (object,), dictionary)
