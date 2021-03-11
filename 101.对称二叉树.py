#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(node1,node2):
            if node1 and node2:
                if node1.val==node2.val:
                    return check(node1.left,node2.right) and check(node1.right,node2.left)
            elif not node1 and not node2:
                return True
            return False

        if root.left and root.right:
            return check(root.left,root.right)
        elif not root.left and not root.right:
            return True
        return False
# @lc code=end

