from collections import Counter, defaultdict
from typing import List


def firstPalindrome(words: List[str]) -> str:
    def is_palindrome(s):
        if len(s) <= 1: return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True

    for w in words:
        if is_palindrome(w):
            return w

    return ""


if __name__ == '__main__':
    s = "1.0.0"
    print(list(map(int, s.split('.'))))
    ss = "abcdefg"
    print(ss[0:3:(-1)])
    stack = [1,2,3]
    print("".join(str(i) for i in stack))
    s1 = "//\\"
    for i in s1:
        print(i)
    res = set([1,3,5,7,9])
    print(list(res))