class Solution:
	def minSubArrayLen(self, target: int, nums) -> int:
		head = 0
		tail = 0

		sum_ = nums[0]

		min_ = len(nums) + 1

		while head < len(nums) and tail < len(nums):
			if sum_ >= target and min_ > head - tail + 1:
				min_ = head - tail + 1
			if head < len(nums) - 1 and sum_ < target:
				head += 1
				sum_ += nums[head]
			elif tail <= head:
				sum_ -= nums[tail]
				tail += 1

		return min_ if min_ <= len(nums) else 0


s = Solution()

target = 15
nums = [1, 2, 3, 4, 5]

print(s.minSubArrayLen(target, nums))
