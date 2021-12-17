import random


class Solution:
	def findPivot(self, nums, l, r):
		if l > r:
			return 0
		m = (r + l) // 2
		if m == r:
			return r
		if nums[m + 1] < nums[m]:
			return m
		if nums[0] > nums[m]:
			return self.findPivot(nums, l, m - 1)
		elif nums[0] < nums[m]:
			return self.findPivot(nums, m + 1, r)

		if l == m:
			return self.findPivot(nums, m + 1, r)

	def binarySearch(self, nums, l, r, target):
		if l > r:
			return -1
		m = (r + l) // 2
		if nums[m] < target:
			return self.binarySearch(nums, m + 1, r, target)
		elif nums[m] > target:
			return self.binarySearch(nums, l, m - 1, target)
		return m

	def search(self, nums, target):
		if len(nums) == 0:
			return -1
		if len(nums) == 1:
			return 0 if nums[0] == target else -1
		pivot = self.findPivot(nums, 0, len(nums) - 1)
		print("pivot  :", pivot)
		if nums[pivot] == target:
			return pivot
		if pivot == 0:
			return self.binarySearch(nums, 1, len(nums) - 1, target)
		if nums[0] < target:
			return self.binarySearch(nums, 0, pivot, target)
		elif nums[0] > target:
			return self.binarySearch(nums, pivot + 1, len(nums) - 1, target)
		return 0



s = Solution()
# for i in range(10000000):
# 	arr_left = sorted(list(set([random.randint(11, 20) for _ in range(random.randint(0, 10))])))
# 	arr_right = sorted(list(set([random.randint(0, 10) for _ in range(random.randint(0, 10))])))
#
# 	arr = arr_left + arr_right
#
# 	target = random.randint(0, 20)
# 	try:
# 		correct = arr.index(target)
# 	except:
# 		correct = -1
# 	answer = s.search(arr, target)
#
# 	if correct != answer:
# 		print(arr)
# 		print("target :", target)
# 		print("correct:", correct)
# 		print("answer :", answer)
# 		break
# 	print("\n\n iter:", i)

arr = [12, 13, 14, 17, 18, 19, 20, 0, 6, 7]
target = 19

print(arr)
try:
	correct = arr.index(target)
except:
	correct = -1
answer = s.search(arr, target)
print("target :", target)
print("correct:", correct)
print("answer :", answer)
