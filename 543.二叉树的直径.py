#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dep(node):
            if not node:
                return 0
            if node.left or node.right:
                return 1+max(dep(node.left),dep(node.right))
            return 1
        if root:
            return max(dep(root.left)+dep(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return 0


# @lc code=end

