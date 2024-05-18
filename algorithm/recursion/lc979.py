from typing import Optional

from algorithm.util.treenode import TreeNode

'''
非常有意思的题目，这并不是一个非常直观的递归
要算这个题目的话，其实可以看每个node要进和出几个coin
对于一个node来说，左子树多了lc个coin，右子树少了rc个coin
那么左子树要把多余的lc传给node，右子树要从node拿rc个coin，所以对于node来说，最小的move是abs(lc) + abs(lr)
node往上传的值就是node.val - 1 + lc + rc
'''
class Solution:
    def __init__(self):
        self.res = 0

    def helper(self, root):
        if not root:
            return 0

        left, right = self.helper(root.left), self.helper(root.right)
        self.res = abs(left) + abs(right)
        return root.val - 1 + left + right

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res