class Solution:
    def checkValidString(self, s: str) -> bool:
        l_stack, star_stack = [], []

        for i in range(len(s)):
            if s[i] == '(':
                l_stack.append(i)
            elif s[i] == ')':
                if not l_stack and not star_stack:
                    return False
                if l_stack:
                    l_stack.pop()
                else:
                    star_stack.pop()
            else: #s[i] == '*'
                star_stack.append(i)

        while l_stack:
            cur = l_stack.pop()
            if not star_stack or star_stack[-1] < cur:
                return False
            star_stack.pop()

        return True


if __name__ == '__main__':
    sol = Solution()
    print(True == sol.checkValidString("()"))
    print(True == sol.checkValidString("(*)"))
    print(True == sol.checkValidString("(*))"))
    print(False == sol.checkValidString("(**))))"))
    print(False == sol.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
    print(False == sol.checkValidString("*("))