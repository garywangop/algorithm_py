from typing import Optional

from algorithm.util.linkedlist import ListNode
from algorithm.util.linkedlist_util import build, isEqual


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        next = head.next
        cur_sum = 0

        while next is not None:
            if next.val == 0:
                node = ListNode(cur_sum)
                prev.next = node
                prev = prev.next
                cur_sum = 0
            else:
                cur_sum += next.val
            next = next.next

        return head.next


if __name__ == '__main__':
    sol = Solution()
    head1, res1 = build([0,3,1,0,4,5,2,0]), build([4,11])
    print(isEqual(sol.mergeNodes(head1), res1))

    head2, res2 = build([0,1,0,3,0,2,2,0]), build([1,3,4])
    print(isEqual(sol.mergeNodes(head2), res2))