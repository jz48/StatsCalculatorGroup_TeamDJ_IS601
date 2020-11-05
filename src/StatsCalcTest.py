import unittest
from StatsCalc import StatsCalculator
from CsvReader import CsvReader
from pprint import pprint



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statsCalculator = StatsCalculator()

    # To test instantiation of calculator class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statsCalculator, StatsCalculator)

    #Testing mean
    def test_mean(self):
        test_data = CsvReader ( './src/data/Mean_Data.csv').data
        for row in test_data:
            self.assertEqual(self.statsCalculator.mean(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), float(row['Mean']))
            self.assertEqual(self.statsCalculator.result, float(row['Mean']))
        test_data.clear()

    #Testing median
    def test_median(self):
        test_data = CsvReader ( './src/data/Median_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.statsCalculator.median(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), float(row['Median']))
            self.assertEqual(self.statsCalculator.result, float(row['Median']))
        test_data.clear()

    #Testing mode
    def test_mode(self):
        test_data = CsvReader ( './src/data/Mode_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.statsCalculator.mode(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), int(row['Mode']))
            self.assertEqual(self.statsCalculator.result, int(row["Mode"]))
        test_data.clear()

    #Testing variance (population)
    def test_variance(self):
        test_data = CsvReader ( './src/data/Variance_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.statsCalculator.variance(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), round(float(row['Variance']), 2))
            self.assertEqual(self.statsCalculator.result, round(float(row['Variance']), 2))
        test_data.clear()

    #Testing standard deviation
    def test_standard_deviation(self):
        test_data = CsvReader ( './src/data/Standard_Deviation_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.statsCalculator.standard_deviation(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), round(float(row['StDev']), 2))
            self.assertEqual(self.statsCalculator.result, round(float(row['StDev']), 2))
        test_data.clear()

    #Testing z-score
    def test_z_score(self):
        test_data = CsvReader ( './src/data/ZScore_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.statsCalculator.z_score(row['Score'], row['Mean'], row['StDev']), round(float(row['Z-Score']), 2))
            self.assertEqual(self.statsCalculator.result, round(float(row['Z-Score']), 2))
        test_data.clear()

if __name__ == '__main__':
    unittest.main()