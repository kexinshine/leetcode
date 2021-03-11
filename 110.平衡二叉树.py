#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node1,dep):
            if node1:
                return max(check(node1.left,dep+1),check(node1.right,dep+1))+1
            return 0
        if not root:
            return True
        if abs(check(root.left,1)-check(root.right,1))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
# @lc code=end

