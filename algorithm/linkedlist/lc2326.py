from typing import Optional, List

from algorithm.util import linkedlist_util
from algorithm.util.linkedlist import ListNode

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        r_start, r_end, c_start, c_end = 0, m - 1, 0, n - 1
        cur_row, cur_col = 0, 0
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir_idx = 0
        while r_start <= cur_row <= r_end and c_start <= cur_col <= c_end:
            if head is None:
                return res
            res[cur_row][cur_col] = head.val
            head = head.next
            next_row, next_col = cur_row + DIR[dir_idx][0], cur_col + DIR[dir_idx][1]

            if cur_row == r_start + 1 and cur_col == c_start:
                r_start += 1
                r_end -= 1
                c_start += 1
                c_end -= 1
                dir_idx = dir_idx + 1 if dir_idx < 3 else 0
                cur_row, cur_col = cur_row + DIR[dir_idx][0], cur_col + DIR[dir_idx][1]
            elif r_start <= next_row <= r_end and c_start <= next_col <= c_end:
                cur_row, cur_col = next_row, next_col
            else:
                dir_idx = dir_idx + 1 if dir_idx < 3 else 0
                cur_row, cur_col = cur_row + DIR[dir_idx][0], cur_col + DIR[dir_idx][1]

        return res


if __name__ == '__main__':
    sol = Solution()
    m1, n1, head1 = 3, 5, linkedlist_util.build([3,0,2,6,8,1,7,9,4,2,5,5,0])
    # print([[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]] == sol.spiralMatrix(m1, n1, head1))

    m2, n2, head2 = 10, 1, linkedlist_util.build([8,24,5,21,10,11,11,12,6,17])
    print([[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]] == sol.spiralMatrix(m2, n2, head2))