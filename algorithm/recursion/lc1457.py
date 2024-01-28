from collections import Counter
from typing import Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import TreeNodeUtil


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        path, res = [], 0

        def is_palindrom(l):
            cnt, odd = Counter(l), 0
            for count in cnt.values():
                if count % 2 != 0:
                    if odd == 1:
                        return False
                    else:
                        odd += 1
            return True

        def helper(root, cur_list):
            if not root.left and not root.right:
                cur_list.append(root.val)
                path.append(cur_list[:])
                cur_list.pop()
                return
            cur_list.append(root.val)
            if root.left:
                helper(root.left, cur_list)
            if root.right:
                helper(root.right, cur_list)
            cur_list.pop()

        helper(root, [])

        for l in path:
            if is_palindrom(l):
                res += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    root1 = TreeNodeUtil([2,3,1,3,1,None,1]).build_treenode()
    print(2 == sol.pseudoPalindromicPaths(root1))

    root2 = TreeNodeUtil([2, 3, 1]).build_treenode()
    print(0 == sol.pseudoPalindromicPaths(root2))
