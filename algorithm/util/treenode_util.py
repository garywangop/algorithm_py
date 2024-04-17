from typing import List
from collections import deque

from algorithm.util.treenode import TreeNode


def build_treenode(l: List[int]):
    if not l:
        return None

    root = TreeNode(l[0])
    q = deque([root])
    index = 1
    while index < len(l):
        cur = q.popleft()
        if index < len(l):
            if l[index]:
                left_node = TreeNode(l[index])
                cur.left = left_node
                q.append(left_node)
            index += 1

        if index < len(l):
            if l[index]:
                right_node = TreeNode(l[index])
                cur.right = right_node
                q.append(right_node)
            index += 1

    return root


def is_equal(node1, node2):
    if not node1 and not node2:
        return True

    if not node1 or not node2:
        return False

    if node1.val != node2.val:
        return False

    return is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)


def test(num):
    print(f"test: {num}")
