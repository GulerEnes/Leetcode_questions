class Solution:
	def countLetters(self, s):
		d = dict()
		for i in s:
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
		return d

	def areDictsSame(self, d1, d2):
		if len(d1) != len(d2):
			return False
		for k1 in d1:
			if k1 not in d2 or d1[k1] != d2[k1]:
				return False
		return True

	def addLetterToDict(self, d, l):
		if l not in d:
			d[l] = 1
		else:
			d[l] += 1

	def popLetterFromDict(self, d, l):
		d[l] -= 1
		if d[l] == 0:
			del d[l]

	def findAnagrams(self, s: str, p: str):
		windowSize = len(p)
		p_counts = self.countLetters(p)
		result = list()

		s_piece_counts = self.countLetters(s[0:windowSize])
		if self.areDictsSame(p_counts, s_piece_counts):
			result.append(0)
		for i in range(1, len(s) - windowSize+1):
			self.addLetterToDict(s_piece_counts, s[i+windowSize-1])
			self.popLetterFromDict(s_piece_counts, s[i-1])

			if self.areDictsSame(p_counts, s_piece_counts):
				result.append(i)
		return result


sol = Solution()

s = "cbaebabac"
p = "abc"
print(sol.findAnagrams(s, p))
