import unittest
from statistics import stdev
from StatsCalc import StatsCalculator
from scipy import stats
from CsvReader import CsvReader
# from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statsCalculator = StatsCalculator()

    # To test instantiation of calculator class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.statsCalculator, StatsCalculator)

    #Testing mean
    def test_mean(self):
        test_data = CsvReader('./src/data/Mean_Data.csv').data
        for row in test_data:
            self.assertEqual(self.statsCalculator.mean(nums=(int(row['Value1']), int(row['Value2']), int(row['Value3']), int(row['Value4']), int(row['Value5']))), float(row['Mean']))
            self.assertEqual(self.statsCalculator.result, float(row['Mean']))
        test_data.clear()

    #Testing median
    def test_median(self):
        test_data = CsvReader('./src/data/Median_Data.csv').data
        # print(test_data)
        for row in test_data:
            data = [float(row['Value1']), float(row['Value2']), float(row['Value3']),
                    float(row['Value4']), float(row['Value5'])]
            # print('data: ', data)
            # print(type(data))
            self.assertEqual(self.statsCalculator.median(data), float(row['Median']))
            self.assertEqual(self.statsCalculator.result, float(row['Median']))
        test_data.clear()

    # Testing mode
    def test_mode(self):
        test_data = CsvReader('./src/data/Mode_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            data = [float(row['Value1']), float(row['Value2']), float(row['Value3']),
                    float(row['Value4']), float(row['Value5'])]
            self.assertEqual(self.statsCalculator.mode(data), float(row['Mode']))
            self.assertEqual(self.statsCalculator.result, float(row["Mode"]))
        test_data.clear()

    #Testing variance (population)
    def test_variance(self):
        test_data = CsvReader('./src/data/Variance_Data.csv').data
        # print(test_data)
        for row in test_data:
            a = self.statsCalculator.variance([int(row['Value1']), int(row['Value2']), int(row['Value3']), int(row['Value4']), int(row['Value5'])])
            b = float(row['Variance'])
            a, b = transformFloat(str(a), str(b))
            self.assertEqual(a, b)

            a = self.statsCalculator.result
            b = float(row['Variance'])
            a, b = transformFloat(str(a), str(b))
            self.assertEqual(a, b)
        test_data.clear()

    # Testing standard deviation
    def test_standard_deviation(self):
        test_data = CsvReader('./src/data/Standard_Deviation_Data.csv').data
        # print(test_data)
        for row in test_data:
            data = [float(row['Value1']), float(row['Value2']), float(row['Value3']), float(row['Value4']), float(row['Value5'])]
            # print('stdev: ', stdev(data))
            self.assertEqual(self.statsCalculator.standard_deviation(data), stdev(data))
            self.assertEqual(self.statsCalculator.result, stdev(data))
        test_data.clear()

    #Testing z-score
    def test_z_score(self):
        test_data = CsvReader('./src/data/ZScore_Data.csv').data
        # print(test_data)
        for row in test_data:
            data1 = float(row['Score'])
            data2 = [float(row['Value1']), float(row['Value2']), float(row['Value3']), float(row['Value4'])]
            data3 = [float(row['Score']), float(row['Value1']), float(row['Value2']), float(row['Value3']),
                     float(row['Value4'])]
            print('z score: ', stats.zscore(data3))
            self.assertEqual(self.statsCalculator.z_score(data1, data3), round(float(row['Z-Score']), 2))
            self.assertEqual(self.statsCalculator.result, round(float(row['Z-Score']), 2))
        test_data.clear()


def transformFloat(a, b):
    a = str(a)[:len(str(b)) - 1]
    b = b[:-1]
    return a, b


if __name__ == '__main__':
    unittest.main()