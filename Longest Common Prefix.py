class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = ''
        default_word = strs[0]
        ind = 0
        while True:
            flag = False
            for word in strs:
                if ind == len(word) or ind == len(default_word) or word[ind] != default_word[ind]:
                    flag = True
                    break
            if flag:
                break
            result += default_word[ind]
            ind += 1
        return result


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
