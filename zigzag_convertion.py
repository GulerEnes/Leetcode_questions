class Solution:
	def f(self, spaces_, s, line_num):
		spaces = spaces_.copy()
		if spaces[0] == 0 and spaces[1] == 0:
			return s[line_num]
		if spaces[0] == 0:
			spaces[0] = spaces[1]
		if spaces[1] == 0:
			spaces[1] = spaces[0]

		res = ""
		flag = 0
		i = line_num

		while i < len(s):
			res += s[i]
			i += spaces[flag]
			flag = 1 if flag == 0 else 0
		return res

	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s
		result = ""
		spaces = [numRows * 2 - 2, 0]
		print(spaces)
		for line_num in range(numRows):
			result += self.f(spaces, s, line_num)

			spaces[0] -= 2
			spaces[1] += 2
		return result


s = Solution()
print(s.convert("AB", 1))