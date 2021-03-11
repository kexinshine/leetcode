#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if pre and pre.val > p.val:
                secondNode = p # 记录第二次逆序的p节点 并跳出循环
                if not firstNode:
                    firstNode = pre # 记录第一次出现逆序的pre节点
                else:
                    break
            pre = p
            p = p.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
# @lc code=end

