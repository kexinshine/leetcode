#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        def check(node1,dep):
            if node1:
                return max(check(node1.left,dep+1),check(node1.right,dep+1))+1
            return 0
        if not root:
            return 0
        return check(root,1)
    




# @lc code=end

