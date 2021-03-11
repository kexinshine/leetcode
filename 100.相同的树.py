#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (not q and p):
            return False
        elif p.left or p.right or q.left or q.right:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) and (p.val==q.val)
        if p.val==q.val:
            return True
        return False 
# @lc code=end

