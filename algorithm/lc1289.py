import heapq
from typing import List


def minFallingPathSum(grid: List[List[int]]) -> int:
    minHeap = [(i, idx) for idx, i in enumerate(grid[0])]
    heapq.heapify(minHeap)

    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            if minHeap[0][1] == j:
                cur = heapq.heappop(minHeap)
                grid[i][j] += minHeap[0][0]
                heapq.heappush(minHeap, cur)
            else:
                grid[i][j] += minHeap[0][0]
        if i + 1 < len(grid):
            minHeap = [(i, idx) for idx, i in enumerate(grid[i])]
            heapq.heapify(minHeap)

    return min(grid[-1])


if __name__ == '__main__':
    grid1 = [[1,2,3],[4,5,6],[7,8,9]]
    grid2 = [[7]]
    grid3 = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
    # print(13 == minFallingPathSum(grid1))
    # print(7 == minFallingPathSum(grid2))
    print(-192 == minFallingPathSum(grid3))

    # minHeap = []
    # heapq.heappush(minHeap, (0, 1))
    # heapq.heappush(minHeap, (1, 1))
    # heapq.heappush(minHeap, (1, 0))
    # while minHeap:
    #     print(heapq.heappop(minHeap))
    #
    # arr = [1, 2, 3]
    # l = [(i, idx) for i, idx in enumerate(arr)]
    # print(l)