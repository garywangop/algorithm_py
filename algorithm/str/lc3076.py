from collections import defaultdict
from typing import List


class Solution:
    def generate_substring(self, l):
        str_set = set()
        for i in range(len(l)):
            for j in range(i + 1, len(l) + 1):
                str_set.add(l[i:j])
        return sorted(list(str_set), key=lambda x: (len(x), x))

    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        m, l, res = defaultdict(int), [], []
        for i in range(len(arr)):
            l.append(self.generate_substring(arr[i]))
            for j in range(len(l[-1])):
                m[l[-1][j]] += 1

        for i in range(len(l)):
            for j in range(len(l[i])):
                if m[l[i][j]] == 1:
                    res.append(l[i][j])
                    break
                elif j == len(l[i]) - 1:
                    res.append("")

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestSubstrings(["gfnt","xn","mdz","yfmr","fi","wwncn","hkdy"]) == ["g","x","z","r","i","c","h"])
    print(sol.shortestSubstrings(["cab","ad","bad","c"]) == ["ab","","ba",""])