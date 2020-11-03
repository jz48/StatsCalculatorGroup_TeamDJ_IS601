from .Calc import Calculator
from .PopSample import cochran, find_sample_size


class PopSampling(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def cochran(self, z, p, q, e):
        self.result = cochran(z, p, q, e)
        return self.result

    def find_sample_size(self, p, q, za2, e):
        self.result = find_sample_size(p, q, za2, e)
        return self.result