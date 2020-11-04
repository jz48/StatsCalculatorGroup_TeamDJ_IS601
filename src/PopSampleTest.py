import unittest
from Calc import Calculator
from PopSample import PopulationSample, cochran, find_sample_size, margin, conf_int

class Popsampling(Calculator):

    def __init__(self):
        super().__init__()


    def cochran(self, z, p, q, e):
        self.result = cochran(z, p, q, e)
        return self.result

    def find_sample_size(self, p, q, za2, e):
        self.result = find_sample_size(p, q, za2, e)
        return self.result

    def margin(self, a, b, c, d, e):
        self.result = margin(a, b, c, d, e)
        return self.result

    def conf_int(self, a, b, c, d, e):
        self.result = conf_int(a, b, c, d, e)
        return self.result

if __name__ == '__main__':
    unittest.main()