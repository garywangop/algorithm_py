from typing import List, Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import build_treenode, is_equal


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []

        def helper(node):
            if node is None:
                return node
            left, right = helper(node.left), helper(node.right)
            if node.val in to_delete:
                if left is not None:
                    res.append(left)
                if right is not None:
                    res.append(right)
                return None
            node.left = left
            node.right = right
            return node

        node = helper(root)
        if node is not None:
            res.append(node)
        return res


if __name__ == '__main__':
    sol = Solution()
    root1, to_delete1, output1 = build_treenode([1, 2, 3, 4, 5, 6, 7]), [3, 5], [build_treenode([1,2,None,4]), build_treenode([6]), build_treenode([7])]
    sol.delNodes(root1, to_delete1)
    # print(is_equal(output1, sol.delNodes(root1, to_delete1)))

    root2, to_delete2, output2 = build_treenode([1,2,4,None,3]), [3], [build_treenode([1,2,4])]
    # print(is_equal(output2, sol.delNodes(root2, to_delete2)))