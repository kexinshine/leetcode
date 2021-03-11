#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            root=TreeNode(root1.val+root2.val)
            root.left=self.mergeTrees(root1.left,root2.left)
            root.right=self.mergeTrees(root1.right,root2.right)
            return root
        elif root1:
            root=TreeNode(root1.val)
            root.left=self.mergeTrees(root1.left,None)
            root.right=self.mergeTrees(root1.right,None)
            return root
        elif root2:
            root=TreeNode(root2.val)
            root.left=self.mergeTrees(root2.left,None)
            root.right=self.mergeTrees(root2.right,None)
            return root
        else:
            return
        


# @lc code=end

