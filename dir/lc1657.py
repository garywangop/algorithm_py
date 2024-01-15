from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        map1, map2 = Counter(word1), Counter(word2)

        keys1 = sorted(map1.keys())
        keys2 = sorted(map2.keys())
        values1 = sorted(map1.values())
        values2 = sorted(map2.values())

        return keys1 == keys2 and values1 == values2


if __name__ == '__main__':
    sol = Solution()
    print(True == sol.closeStrings("abc", "bca"))
    print(False == sol.closeStrings("cabbba", "aabbss"))
