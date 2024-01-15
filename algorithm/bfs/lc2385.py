from collections import deque
from typing import Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import TreeNodeUtil


class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        startNode, q = Node(), deque()

        q.append(root)

        while q:
            cur = q.popleft()
            if cur.val == start:
                startNode 

        res = 0
        q.append(startNode)
        visited = set()
        visited.add(startNode.val)

        while q:
            res += 1
            cur = q.popleft()
            if cur.parent and cur.parent.val not in visited:
                q.append(cur.parent)
                visited.add(cur.parent.val)
            if cur.left and cur.left.val not in visited:
                q.append(cur.left)
                visited.add(cur.left.val)
            if cur.right and cur.right.val not in visited:
                q.append(cur.right)
                visited.add(cur.right.val)

        return res


if __name__ == '__main__':
    sol = Solution()
    root1 = TreeNodeUtil([1,5,3,None,4,10,6,9,2]).build_treenode()
    print(4 == sol.amountOfTime(root1, 3))