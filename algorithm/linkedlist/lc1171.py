from typing import Optional

from algorithm.util.linkedlist import ListNode
from algorithm.util.linkedlist_util import build, isEqual


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        nodes = {0: dummy}
        dummy.next = head
        prev = dummy
        cur_sum = 0

        while head:
            if head.val == 0:
                prev.next = head.next
                head = head.next
                continue
            cur_sum += head.val
            if cur_sum in nodes:
                prev = nodes[cur_sum]
                cur_node = prev.next
                tmp_sum = cur_sum
                while cur_node != head:
                    tmp_sum += cur_node.val
                    nodes.pop(tmp_sum)
                    cur_node = cur_node.next
                prev.next = head.next
                head = head.next
            else:
                nodes[cur_sum] = head
                prev = head
                head = head.next

        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    head1 = build([1, 2, 3, -3, 4])
    head2 = build([1,2,-3,3,1])

    print(isEqual(sol.removeZeroSumSublists(head1), build([1, 2, 4])))
    print(isEqual(sol.removeZeroSumSublists(head2), build([3,1])))
