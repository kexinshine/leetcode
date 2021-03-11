#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=list()
    def sumNumbers(self, root: TreeNode) -> int:
        self.recursion(root,0)
        return sum(self.ans)


    def recursion(self,root,val):
        if not root.left and not root.right:
            self.ans.append(val+root.val)
        if root.left:
            temp=root.val*10+val*10
            self.recursion(root.left,temp)
        if root.right:
            temp=root.val*10+val*10
            self.recursion(root.right,temp)
        

        
# @lc code=end

