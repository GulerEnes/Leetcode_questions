class Solution:
	def bruteforce(self, height):
		max_ = 0
		for i in range(len(height)):
			for j in range(i + 1, len(height)):
				A = min(height[i], height[j]) * (j - i)
				if A > max_:
					max_ = A
		return max_

	def maxArea(self, height):
		l = 0
		r = len(height) - 1

		max_ = 0
		while l != r:
			A = min(height[l], height[r]) * (r - l)
			if A > max_:
				max_ = A
			if height[l] < height[r]:
				l += 1
			else:
				r -= 1
		return max_


s = Solution()
inp = [2, 3, 4, 5, 18, 17, 6]
print(s.bruteforce(inp))
print(s.maxArea(inp))
