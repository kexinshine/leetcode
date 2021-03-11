#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check_left(node, n):
            if node.val>=n:
                return False
            if node.left and node.right:
                return (check_left(node.left,n) and check_left(node.right,n))
            elif node.left:
                return check_left(node.left,n) 
            elif node.right:
                return check_left(node.right,n)
            else:
                return True
        def check_right(node, n):
            if node.val<=n:
                return False
            if node.left and node.right:
                return (check_right(node.left,n) and check_right(node.right,n))
            elif node.left:
                return check_right(node.left,n) 
            elif node.right:
                return check_right(node.right,n)
            else:
                return True
        if root.left and root.right:
            if check_left(root.left,root.val) and check_right(root.right,root.val):
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            return False
        elif root.left:
            if check_left(root.left,root.val):
                return self.isValidBST(root.left)
            return False
        elif root.right:
            if check_right(root.right,root.val):
                return self.isValidBST(root.right)
            return False
        return True


# @lc code=end

