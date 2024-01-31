from typing import List

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res, stack = [0 for _ in range(len(t))], []

        for i in range(len(t)):
            while stack and t[i] > stack[-1][0]:
                cur = stack.pop()
                res[cur[1]] = i - cur[1]
            stack.append((t[i], i))

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])
    print(sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0])
    print(sol.dailyTemperatures([30,60,90]) == [1,1,0])