from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False


class Solution:

    def build(self, words):
        root = TrieNode()
        cur = root
        for word in words:
            for l in word:
                idx = ord(l) - ord('a')
                if not cur.children[idx]:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.is_word = True
            cur = root
        return root

    def dfs(self, root: TrieNode, node: TrieNode, cur: str, idx: int, s: str, res: List[str]) -> None:
        if idx == len(s):
            if node.is_word:
                res.append(cur[:])
            return

        node_idx = ord(s[idx]) - ord('a')
        if not node.children[node_idx]:
            return

        node = node.children[node_idx]
        cur += s[idx]
        if node.is_word:
            self.dfs(root, node, cur, idx + 1, s, res)

            cur += " "
            self.dfs(root, root, cur, idx + 1, s, res)
            cur = cur[:-1]
        else:
            self.dfs(root, node, cur, idx + 1, s, res)
        cur = cur[:-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = self.build(wordDict)
        res = []
        self.dfs(root, root, "", 0, s, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    s1, wordDict1, res1 = "catsanddog", ["cat", "cats", "and", "sand", "dog"], ["cats and dog", "cat sand dog"]
    print(sorted(res1) == sorted(sol.wordBreak(s1, wordDict1)))

    s2, wordDict2, res2 = "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"], [
        "pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    print(sorted(res2) == sorted(sol.wordBreak(s2, wordDict2)))

    s3, wordDict3, res3 = "catsandog", ["cats", "dog", "sand", "and", "cat"], []
    print(sorted(res3) == sorted(sol.wordBreak(s3, wordDict3)))

    s4, wordDict4, res4 = "abc", ["ab", "abc", "c"], ["abc", "ab c"]
    print(sorted(res4) == sorted(sol.wordBreak(s4, wordDict4)))

