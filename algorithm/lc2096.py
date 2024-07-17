from typing import Optional

from algorithm.util.treenode import TreeNode
from algorithm.util.treenode_util import build_treenode


class Solution:
    """
    这个题目还蛮有意思的
    我第一反应是用LCA来做，但是后来看了Neetcode的视频，他提供了一个新的思路
    其实只要以root为起始点，找到start和dest在哪
    找到之后，把重复路径消除就行了

    这个题目的path我原本是用str来写的，但是LC会超时，用list不会超时
    """
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(cur, path, target):
            if cur is None:
                return []
            if cur.val == target:
                return path

            # search left
            path.append("L")
            res = dfs(cur.left, path, target)
            if res:
                return res
            path.pop()
            # search right
            path.append("R")
            res = dfs(cur.right, path, target)
            if res:
                return res
            path.pop()
            return []

        startPath, endPath = dfs(root, [], startValue), dfs(root, [], destValue)
        idx = 0
        while idx < min(len(startPath), len(endPath)) and startPath[idx] == endPath[idx]:
            idx += 1
        res = ""
        for _ in range(idx, len(startPath)):
            res += "U"
        res += "".join(endPath[idx:])
        return res


if __name__ == '__main__':
    sol = Solution()
    root1, startValue1, destValue1 = build_treenode([5,1,2,3,None,6,4]), 3, 6
    print("UURL" == sol.getDirections(root1, startValue1, destValue1))

    root2, startValue2, destValue2 = build_treenode([2, 1]), 2, 1
    print("L" == sol.getDirections(root2, startValue2, destValue2))

    root3, startValue3, destValue3 = build_treenode([1,None,10,12,13,4,6,None,15,None,None,5,11,None,2,14,7,None,8,None,None,None,9,3]), 6, 15
    print("UURR" == sol.getDirections(root3, startValue3, destValue3))

