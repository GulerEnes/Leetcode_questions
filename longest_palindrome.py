class Solution:
	def f(self, l, r, s):
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l + 1:r]

	def longestPalindrome(self, s: str) -> str:
		result = ""
		for m in range(len(s)):
			temp = self.f(m, m, s)
			if len(temp) > len(result):
				result = temp
			temp = self.f(m, m+1, s)
			if len(temp) > len(result):
				result = temp
		return result


s = Solution()
print(s.longestPalindrome(
	"xaxa"))
