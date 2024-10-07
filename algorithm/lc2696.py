class Solution:
    def minLength(self, s: str) -> int:
        res, stack = 0, []
        for i in s:
            if i == 'D' and stack and stack[-1] == 'C':
                stack.pop()
                res += 1
            elif i == 'B' and stack and stack[-1] == 'A':
                stack.pop()
                res += 1
            else:
                stack.append(i)
        return len(s) - res * 2


if __name__ == '__main__':
    sol = Solution()
    print(2 == sol.minLength("ABFCACDB"))