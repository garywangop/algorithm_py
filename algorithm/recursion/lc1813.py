from collections import deque


class Node:
    def __init__(self, val=""):
        self.is_word = False
        self.val = val
        self.children = []


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        def build_prefix(arr):
            res = [arr]
            prefix = ""
            for i in range(len(arr)):
                if arr[i] == " ":
                    res.append(prefix)
                prefix += arr[i]
            return res

        def build_suffix(arr):
            res = [arr]
            suffix = ""
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] == " ":
                    res.append(suffix)
                suffix = arr[i] + suffix
            return res

        s = sentence1 if len(sentence1) < len(sentence2) else sentence2
        l = sentence1 if s == sentence2 else sentence2

        l_prefix, l_suffix = build_prefix(l), build_suffix(l)

        for i in range(len(s)):
            if s[i] == " ":
                prefix, suffix = s[:i], s[i + 1:]
                if prefix in l_prefix and suffix in l_suffix:
                    return True

        # whole s as a prefix or whole s as a suffix
        if s in l_prefix or s in l_suffix:
            return True

        return False




if __name__ == '__main__':
    sol = Solution()

    sentence1 = "My name is Haley"
    sentence2 = "My Haley"
    # print(True == sol.areSentencesSimilar(sentence1, sentence2))

    s1, s2 = "C wook", "aIhTrm MF Nm C dIFNN wook r sBj GljQh E GpgvYh P"
    print(False == sol.areSentencesSimilar(s1, s2))
