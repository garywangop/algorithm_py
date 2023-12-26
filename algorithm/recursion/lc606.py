from typing import Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import TreeNodeUtil


class Solution:
    def tree2str(self, node: Optional[TreeNode]) -> str:

        def helper(root):
            if root is None:
                return ""

            left = helper(root.left)
            right = helper(root.right)

            if left and right:
                return f"({root.val}{left}{right})"
            elif left or right:
                return f"({root.val}{left})" if left else f"({root.val}(){right})"
            else:
                return f"({root.val})"

        return helper(node)[1:-1]


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    root = TreeNodeUtil(l).build_treenode()
    sol = Solution()
    print(sol.tree2str(root))
