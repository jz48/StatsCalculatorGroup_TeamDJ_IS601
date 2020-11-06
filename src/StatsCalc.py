from statistics import mode

from Calc import Calculator


class StatsCalculator(Calculator):
	result = 0
	
	def __init__(self):
		super().__init__()

	def mean(self, nums):
		res = 0
		counter = 0
		for i in nums:
			res = self.add(res, i)
			counter = counter + 1
		return self.division(counter, res)

	def median(self, nums):
		# print('nums: ', nums, type(nums))
		nums = sorted(nums)
		# print('nums: ', nums, type(nums))
		# print('len: ', len(nums), self.mode(2, len(nums)))
		if self.mode(2, len(nums)) == 1:
			self.result = nums[int(self.division(2, (len(nums)+1)))-1]
		else:
			self.result = self.division(2, nums[int(self.division(2, (len(nums)+1)))-1]+nums[int(self.division(2, (len(nums)+1))-1)-1])
		return self.result

	def mode(self, a, b):
		# print('a, b: ', a, b)
		b = b - self.multiplication(a, (int(self.division(a, b))))
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
		m = self.mean(nums)
		res = 0
		for i in nums:
			res = res + self.multiplication(i - m, i - m)
		res = self.division(len(nums), res)
		return res

	def z_score(self, x, nums):
		m = self.mean(nums)
		a = self.subtract(m, x)
		b = self.standard_deviation(nums)
		z = self.division(b, a)
		return z


if __name__ == '__main__':
	sc = StatsCalculator()
	print(sc.mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
