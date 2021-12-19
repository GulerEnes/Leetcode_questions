class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		si = len(s) - 1
		ti = len(t) - 1

		not_compare_count_s = 0
		not_compare_count_t = 0

		while si >= 0 or ti >= 0:
			# Found comparable letter on s
			is_comparable_s = False
			while not is_comparable_s and si >= 0:
				debug_s = s[si]
				if s[si] == '#':
					not_compare_count_s += 1
					si -= 1
				else:
					if not_compare_count_s == 0:
						is_comparable_s = True
					else:
						si -= 1
						not_compare_count_s -= 1

			# Found comparable letter on t
			is_comparable_t = False
			while not is_comparable_t and ti >= 0:
				debug_t = t[ti]
				if t[ti] == '#':
					not_compare_count_t += 1
					ti -= 1
				else:
					if not_compare_count_t == 0:
						is_comparable_t = True
					else:
						ti -= 1
						not_compare_count_t -= 1

			if si < 0 and ti < 0:
				return True
			if si < 0 or ti < 0:
				return False
			if s[si] != t[ti]:
				return False
			si -= 1
			ti -= 1

		return False if si != ti or (si > 0 or ti > 0) else True


sol = Solution()

s = "j##yc##bs#srqpfzantto###########i#mwb"
t = "j##yc##bs#srqpf#zantto###########i#mwb"

print(sol.backspaceCompare(s, t))

