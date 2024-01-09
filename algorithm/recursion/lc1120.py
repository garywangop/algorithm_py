import random
from typing import Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import TreeNodeUtil


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0

        def helper(root):
            if not root:
                return 0, 0

            left_sum, left_node_count = helper(root.left)
            right_sum, right_node_count = helper(root.right)
            cur_sum, cur_node_count = left_sum + right_sum + root.val, left_node_count + right_node_count + 1

            self.res = max(self.res, cur_sum / cur_node_count)
            return cur_sum, cur_node_count

        helper(root)
        return self.res



if __name__ == '__main__':
    root = TreeNodeUtil([5,6,1]).build_treenode()
    sol = Solution()
    print(sol.maximumAverageSubtree(root))