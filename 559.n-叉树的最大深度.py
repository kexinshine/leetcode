#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dep(node,depth):
            if not node.children:
                return depth
            max_dep=0
            for child in node.children:
                max_dep=max(dep(child,depth+1),max_dep)
            return max_dep
        if not root:
            return 0
        return dep(root,1)


# @lc code=end

