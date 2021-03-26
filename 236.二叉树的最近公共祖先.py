#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root==p or root==q or not root:
            return root
        p_left=self.lowestCommonAncestor(root.left,p,q)
        q_right=self.lowestCommonAncestor(root.right,p,q)
        if not p_left:
            return q_right
        if not q_right:
            return p_left
        return root

# @lc code=end

