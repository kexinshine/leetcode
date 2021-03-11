#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
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
        self.ans=[[]]
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.ans[0]=[root.val]
        if root.left or root.right:
            self.gogogo(root.left,root.right,1)
        res=[x for x in self.ans if x!=[]]
        return list(reversed(res))
    def gogogo(self,node1,node2,dep):
        self.ans.append([])
        if node1:
            self.ans[dep].append(node1.val)
            if node1.left or node1.right:
                self.gogogo(node1.left,node1.right,dep+1)
        if node2: 
            self.ans[dep].append(node2.val)
            if node2.left or node2.right:
                self.gogogo(node2.left,node2.right,dep+1)
# @lc code=end

