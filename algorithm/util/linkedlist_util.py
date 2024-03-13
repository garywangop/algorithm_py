from typing import List

from algorithm.util.linkedlist import ListNode


def build(l: List[int]) -> ListNode:
    dummy = ListNode(0)
    head = dummy
    for i in l:
        node = ListNode(i)
        head.next = node
        head = head.next
    return dummy.next


def isEqual(head1: ListNode, head2: ListNode) -> bool:
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1, head2 = head1.next, head2.next

    return True if not head1 and not head2 else False
