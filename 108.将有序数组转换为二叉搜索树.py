#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        len_nums=len(nums)
        m=int(len_nums/2)
        if len_nums>1:
            head=TreeNode(nums[m])
            head.left=self.sortedArrayToBST(nums[:m])
            head.right=self.sortedArrayToBST(nums[m+1:])
            return head
        elif len_nums==1:
            head=TreeNode(nums[m])
            return head
        return

# @lc code=end

