from typing import List
from collections import deque

from algorithm.util.treenode import TreeNode


class TreeNodeUtil:
    def __init__(self, l: List[int]):
        self.l = l

    def build_treenode(self):
        if not self.l:
            return None

        root = TreeNode(self.l[0])
        q = deque([root])
        index = 1
        while index < len(self.l):
            cur = q.popleft()
            if index < len(self.l) and self.l[index]:
                left_node = TreeNode(self.l[index])
                cur.left = left_node
                q.append(left_node)
                index += 1

            if index < len(self.l) and self.l[index]:
                right_node = TreeNode(self.l[index])
                cur.right = right_node
                q.append(right_node)
                index += 1

        return root
