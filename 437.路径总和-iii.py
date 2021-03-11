#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count=0
        def dfs(root,val):
            nonlocal sum
            nonlocal count
            if not root:
                return
            temp=root.val+val
            if temp==sum:
                count+=1
            dfs(root.left,temp)
            dfs(root.right,temp)
        def bfs(root):
            if root:
                dfs(root,0)
                bfs(root.left)
                bfs(root.right)
            return
        bfs(root)
        return count

        
# @lc code=end

