from typing import Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import build_treenode, is_equal, test


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root

        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        if depth == 2:
            node1, node2 = TreeNode(val), TreeNode(val)
            node1.left, node2.right = root.left, root.right
            root.left, root.right = node1, node2
            return root

        self.addOneRow(root.left, val, depth - 1)
        self.addOneRow(root.right, val, depth - 1)
        return root


if __name__ == '__main__':
    sol = Solution()
    root1 = build_treenode([4,2,6,3,1,5])
    output1 = build_treenode([4,1,1,2,None,None,6,3,1,5])
    print(is_equal(sol.addOneRow(root1, 1, 2), output1))
    root2 = build_treenode([4,2,None,3,1])
    print(is_equal(sol.addOneRow(root2, 1, 3), build_treenode([4,2,None,1,1,3,None,None,1])))
    root3 = build_treenode([4,2,6,3,1,5])
    output3 = build_treenode([4,2,6,3,1,5,None,1,1,1,1,1,1])
    print(is_equal(sol.addOneRow(root3, 1, 4), output3))