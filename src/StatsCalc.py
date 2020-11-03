from Calc import Calculator


class StatsCalculator(Calculator):
	def __init__(self):
		super().__init__()

	def mean(self, nums):
		res = 0
		cnt = 0
		for i in nums:
			res = self.add(res, i)
			cnt = cnt + 1
		return res/cnt


if __name__ == '__main__':
	sc = StatsCalculator()
	print(sc.mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
