import random


class random_generator():
	def __init__(self):
		pass

	def GenNum_noSeed(self, l, r):
		return random.uniform(l, r)

	def GenNum_withSeed(self, l, r, seed):
		random.seed(seed)
		return random.uniform(l, r)

	def GenList_withSeed(self, l, r, seed, N):
		random.seed(seed)
		return [random.uniform(l, r) for _ in range(N)]

	def ListItem_noSeed(self, arr):
		return arr[random.randint(0, len(arr))]

	def ListItem_withSeed(self, arr, seed):
		random.seed(seed)
		return arr[random.randint(0, len(arr))]

	def ListItemN_noSeed(self, arr, N):
		return [arr[random.randint(0, len(arr)-1)] for _ in range(N)]

	def ListItemN_withSeed(self, arr, seed, N):
		random.seed(seed)
		return [arr[random.randint(0, len(arr)-1)] for _ in range(N)]


def main():
	rg = random_generator()
	print('1 no', rg.GenNum_noSeed(0, 100))
	print('1 no', rg.GenNum_noSeed(0, 100))
	print('1 wi 9', rg.GenNum_withSeed(9, 0, 100))
	print('1 wi 9', rg.GenNum_withSeed(9, 0, 100))
	print('1 wi 13', rg.GenNum_withSeed(13, 0, 100))
	print('1 wi 19', rg.GenNum_withSeed(19, 0, 100))
	print('n 13', rg.GenList_withSeed(13, 0, 100, 10))
	print('n 13', rg.GenList_withSeed(13, 0, 100, 20))
	print('n 19', rg.GenList_withSeed(19, 0, 100, 10))

	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	print('li no', rg.ListItem_noSeed(arr))
	print('li no', rg.ListItem_noSeed(arr))
	print('li no', rg.ListItem_noSeed(arr))
	print('li wi 19', rg.ListItem_withSeed(arr, 19))
	print('li wi 19', rg.ListItem_withSeed(arr, 19))
	print('li wi 37', rg.ListItem_withSeed(arr, 37))
	print('li wi 59', rg.ListItem_withSeed(arr, 58))

	print('li no', rg.ListItemN_noSeed(arr, 20))
	print('li no', rg.ListItemN_noSeed(arr, 20))
	print('li no', rg.ListItemN_noSeed(arr, 33))
	print('li wi 19', rg.ListItemN_withSeed(arr, 19, 6))
	print('li wi 19', rg.ListItemN_withSeed(arr, 19, 9))
	print('li wi 37', rg.ListItemN_withSeed(arr, 37, 6))
	print('li wi 59', rg.ListItemN_withSeed(arr, 58, 6))


if __name__ == '__main__':
	main()
