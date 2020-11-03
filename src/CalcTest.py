import unittest
from Calc import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        print('---------------test addition------------------')
        test_data = CsvReader('./src/data/UnitTestAddition.csv').data
        # print(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtraction(self):
        print('---------------test subtraction------------------')
        # find out bugs successfully
        test_data = CsvReader('./src/data/UnitTestSubtraction.csv').data
        # print(test_data)
        for row in test_data:
            # print(int(row['Value 1']), int(row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        print('---------------test multiplication------------------')
        test_data = CsvReader('./src/data/UnitTestMultiplication.csv').data
        # print(test_data)
        for row in test_data:
            # print(int(row['Value 1']), int(row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.multiplication(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        print('---------------test division------------------')
        # find out bugs successfully
        test_data = CsvReader('./src/data/UnitTestDivision.csv').data
        for row in test_data:
            a, b = transformFloat(self.calculator.division(int(row['Value 1']), int(row['Value 2'])), row['Result'])
            self.assertEqual(a, b)

            a, b = transformFloat(self.calculator.result, row['Result'])
            self.assertEqual(a, b)

    def test_square(self):
        print('---------------test square------------------')
        test_data = CsvReader('./src/data/UnitTestSquare.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squareRoot(self):
        print('---------------test square root------------------')
        # find out bugs successfully
        test_data = CsvReader('./src/data/UnitTestSquareRoot.csv').data
        for row in test_data:
            a, b = transformFloat(self.calculator.root(int(row['Value 1'])), row['Result'])
            self.assertEqual(a, b)

            a, b = transformFloat(self.calculator.result, row['Result'])
            self.assertEqual(a, b)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


def transformFloat(a, b):
    a = str(a)[:len(str(b)) - 1]
    b = b[:-1]
    return a, b


if __name__ == '__main__':
    unittest.main()
