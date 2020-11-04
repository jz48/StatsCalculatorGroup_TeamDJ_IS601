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

	def median(self, nums):
		nums = nums.sort()
		if mode(len(nums), 2) == 1:
			res = nums[self.division(2, (len(nums)+1))]
		else:
			res = self.division(2, nums[self.division(2, (len(nums)+1))]+nums[self.division(2, (len(nums)+1))-1])
		return res

	def mode(self, a, b):
		b = b - self.multiplication(a, (self.dicision(a, b)))
		return b

	def standard_deviation(self, nums):
		m = self.mean(nums)
		res = 0
		for i in nums:
			res = res + self.multiplication(i - m, i - m)
		res = self.root(res)
		res = self.division(len(nums), res)
		return res

	def variance(self, nums):
		pass

	def z_score(self, x, nums):
		pass


if __name__ == '__main__':
	sc = StatsCalculator()
	print(sc.mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
