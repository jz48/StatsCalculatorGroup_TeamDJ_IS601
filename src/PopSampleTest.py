import unittest
from PopSample import PopulationSample
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.PopulationSample = PopulationSample()

    # To test instantiation of PopSampling class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.PopulationSample, PopulationSample)

    # Testing Cochran
    def test_cochran(self):
        test_data = CsvReader('./src/data/Cochran_Data.csv').data
        for row in test_data:
            #pprint(self.PopSampling.cochran(row['Z'], row['p'], row['q'], row['e']))
            self.assertEqual(self.PopulationSample.cochran(row['Z'], row['p'], row['q'], row['e']), int(row['Sample']))
            self.assertEqual(self.PopulationSample.result, int(row['Sample']))
        test_data.clear()

    # Testing FindSample
    def test_find_sample_size(self):
        test_data = CsvReader('./src/data/FindSample_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopulationSample.find_sample_size(row['P'], row['q'], row['za2'], row['e']), int(row['Sample']))
            self.assertEqual(self.PopulationSample.result, int(row['Sample']))
        test_data.clear()

    # Testing MarginOfError
    def test_margin(self):
        test_data = CsvReader('./src/data/Margin_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopulationSample.margin(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), float(row['Error']))
            self.assertEqual(self.PopulationSample.result, float(row['Error']))
        test_data.clear()

    # Testing ConfidenceInterval
    def test_conf_int(self):
        test_data = CsvReader('./src/data/ConfInt_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopulationSample.conf_int(row['a'], row['b'], row['c'], row['d'], row['e']), float(row['ConfInt']))
            self.assertEqual(self.PopulationSample.result, float(row['ConfInt']))
        test_data.clear()