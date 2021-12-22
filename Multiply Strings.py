class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        arr = []

        for i in range(len(num1) - 1, -1, -1):
            hold = 0
            temp = ''
            for j in range(len(num2) - 1, -1, -1):
                x = int(num1[i]) * int(num2[j])
                temp = str(x % 10 + hold) + temp
                hold = x // 10
            temp = str(hold) + temp
            arr.append(temp)

        for i in range(len(arr)):
            arr[i] += '0' * i
            arr[i] = '0' * (len(num1) - i - 1) + arr[i]

        if len(arr) == 1:
            while arr[0][i] == '0':
                i += 1
            return arr[0][i:]
        result = ''
        print(arr)
        hold = 0
        for i in range(len(arr[0]) - 1, -1, -1):
            x = hold
            for j in range(len(arr)):
                x += int(arr[j][i])
            result = str(x % 10) + result
            hold = x // 10
        result = str(hold) + result

        i = 0
        while result[i] == '0':
            i += 1
        return result[i:]


s = Solution()

num1 = "999"
num2 = "999"

print(s.multiply(num1, num2))