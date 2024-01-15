from typing import Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import TreeNodeUtil


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = -1

        def helper(node):
            if not node.left and not node.right:
                return node.val, node.val

            cur = node.val, node.val

            if not node.left:
                cur = min(node.val, helper(node.right)[0]), max(node.val, helper(node.right)[1])

            if not node.right:
                cur = min(node.val, helper(node.left[0])), max(node.val, helper(node.left)[1])

            self.res = max(self.res, abs(cur[0] - cur[1]))
            return cur

        helper(root)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    root1 = TreeNodeUtil([8,3,10,1,6,None,14,None,None,4,7,13]).build_treenode()
    print(7 == sol.maxAncestorDiff(root1))
    root2 = TreeNodeUtil([1,2]).build_treenode()
    print(1 == sol.maxAncestorDiff(root2))