from collections import Counter, defaultdict
from typing import List


'''
下面是错误的
'''
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        m = Counter(letters)
        res = 0

        for word in words:
            cur, visited = 0, defaultdict(int)
            for l in word:
                if l not in m or (l in visited and visited[l] >= m[l]):
                    cur = 0
                    break
                visited[l] += 1
                cur += score[ord(l) - ord('a')]
            res = max(res, cur)
        return res


if __name__ == '__main__':
    sol = Solution()
    words1 = ["dog", "cat", "dad", "good"]
    letters1 = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score1 = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(23 == sol.maxScoreWords(words1, letters1, score1))
