"""

HENÜZ ÇÖZÜLEMEDİ

"""

class Solution:
	def numSubarrayProductLessThanK(self, nums, k):
		result = 0

		for window_size in range(1, len(nums) + 1):
			product = 1
			for i in range(window_size):
				product *= nums[i]
			if product < k:
				result += 1

			for i in range(window_size, len(nums)):
				product /= nums[i - window_size]
				product *= nums[i]

				if product < k:
					result += 1
		return result


s = Solution()

nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
k = 19

print(s.numSubarrayProductLessThanK(nums, k))
