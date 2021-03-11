#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def check(node1,dep):
            if node1 and node1.left and node1.right:
                return min(check(node1.left,dep+1),check(node1.right,dep+1))+1
            elif node1 and node1.left:
                return check(node1.left,dep+1)+1
            elif node1 and node1.right:
                return check(node1.right,dep+1)+1
            return 1
        if not root: 
            return 0
        return check(root,1)
# @lc code=end

