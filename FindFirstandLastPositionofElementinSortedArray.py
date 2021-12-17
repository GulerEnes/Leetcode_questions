import random


class Solution:
	def bruteForce(self, nums, target):
		try:
			return [nums.index(target), len(nums)-nums[::-1].index(target)-1]
		except:
			return [-1, -1]

	def binarySearchWithNeigboor(self, whichNeighboor, arr, target, l, r):
		# whichNeighboor: left side = -1, right side = 1
		if l > r:
			return -1
		m = (r + l) // 2
		if arr[m] < target:
			return self.binarySearchWithNeigboor(whichNeighboor, arr, target, m+1, r)
		elif arr[m] > target:
			return self.binarySearchWithNeigboor(whichNeighboor, arr, target, l, m-1)
		else:  # arr[m] == target
			neighboor = m + whichNeighboor
			if 0 <= neighboor < len(arr):
				if arr[neighboor] != target:
					return m
				else:
					if whichNeighboor == -1:
						return self.binarySearchWithNeigboor(whichNeighboor, arr, target, l, m-1)
					else:
						return self.binarySearchWithNeigboor(whichNeighboor, arr, target, m+1, r)
			else:
				return m


	def searchRange(self, nums, target):
		# if len(nums) == 1:
		# 	if target == nums[0]:
		# 		return [0, 0]
		# 	return [-1, -1]
		left = self.binarySearchWithNeigboor(-1, nums, target, 0, len(nums) - 1)
		right = self.binarySearchWithNeigboor(1, nums, target, 0, len(nums) - 1)

		return [left, right]


if __name__ == '__main__':
	for i in range(1000000):

		arr = sorted([random.randint(0, 15) for _ in range(random.randint(0, 20))])
		target = random.randint(0, 15)


		# arr = [2]
		# target = 2
		# print([i for i in range(0, 20)])
		print(arr, "  target:", target)
		s = Solution()

		real = s.searchRange(arr, target)
		brute = s.bruteForce(arr, target)
		print("real : ", real)
		print("brute: ", brute)

		print("\n\n ", i)

		if real[0] != brute[0] or real[1] != brute[1]:
			break
