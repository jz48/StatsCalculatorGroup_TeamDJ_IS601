import unittest
from PopSample import PopulationSample
from CsvReader import CsvReader
# from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.PopulationSample = PopulationSample()

    # To test instantiation of PopSampling class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.PopulationSample, PopulationSample)

    # Testing Cochran
    def test_cochran(self):
        print('---------------test cochran-----------------')
        test_data = CsvReader('./src/data/Cochran_Data1.csv').data
        for row in test_data:
            # pprint(self.PopSampling.cochran(row['Z'], row['p'], row['q'], row['e']))
            self.assertEqual(self.PopulationSample.cochran(float(row['z']), float(row['p']), float(row['q']), float(row['e'])), int(row['Sample']))
            self.assertEqual(self.PopulationSample.result, int(row['Sample']))
        test_data.clear()

    # Testing FindSample
    def test_find_sample_size(self):
        print('---------------test find sample size-----------------')
        test_data = CsvReader('./src/data/FindSample_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopulationSample.find_sample_size(row['P'], row['q'], row['za2'], row['e']), int(row['Sample']))
            self.assertEqual(self.PopulationSample.result, int(row['Sample']))
        test_data.clear()

    # Testing MarginOfError
    def test_margin(self):
        print('---------------test margin-----------------')
        test_data = CsvReader('./src/data/Margin_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopulationSample.margin(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), float(row['Error']))
            self.assertEqual(self.PopulationSample.result, float(row['Error']))
        test_data.clear()

    # Testing ConfidenceInterval
    def test_conf_int(self):
        print('---------------test conf int-----------------')
        test_data = CsvReader('./src/data/ConfInt_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopulationSample.conf_int(row['a'], row['b'], row['c'], row['d'], row['e']), float(row['ConfInt']))
            self.assertEqual(self.PopulationSample.result, float(row['ConfInt']))
        test_data.clear()


if __name__ == '__main__':
    unittest.main()
