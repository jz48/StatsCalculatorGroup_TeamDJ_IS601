import unittest
from CsvReader import CsvReader, ClassFactory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('./src/data/testData.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('employee')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('employee', self.csv_reader.data[0])
        for person in people:
            # print(test_class, person)
            # print(person.__name__, test_class.__name__)
            self.assertEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
