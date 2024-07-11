class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                cur = ""
                while stack and stack[-1] != "(":
                    cur += stack.pop()
                stack.pop() # pop the top "("
                stack.extend(cur)
                print(stack)
        return "".join(str(i) for i in stack)


if __name__ == '__main__':
    sol = Solution()
    s1, res1 = "(abcd)", "dcba"
    # print(res1 == sol.reverseParentheses(s1))

    s2, res2 = "(u(love)i)", "iloveu"
    print(res2 == sol.reverseParentheses(s2))