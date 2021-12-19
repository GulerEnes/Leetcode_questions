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

	def findMin(self, nums) -> int:
		if len(nums) == 1:
			return nums[0]
		pvt = self.findPivot(nums, 0, len(nums) - 1)
		return nums[(pvt + 1) % len(nums)]


if __name__ == '__main__':
	s = Solution()

	for i in range(100000):
		arr_left = sorted(list(set([random.randint(11, 20) for _ in range(random.randint(1, 10))])))
		arr_right = sorted(list(set([random.randint(0, 10) for _ in range(random.randint(1, 10))])))

		arr = arr_left + arr_right

		target = random.randint(0, 20)
		try:
			correct = min(arr)
		except:
			correct = -1
		answer = s.findMin(arr)

		if correct != answer:
			print(arr)
			print("correct:", correct)
			print("answer :", answer)
			break
		print("\n\n iter:", i)
