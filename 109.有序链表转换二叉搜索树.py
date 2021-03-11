#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        m=int(length/2)
        if length>1:
            temp=head
            while m>1:
                temp=temp.next
                m-=1
            ans=temp.next.next
            root=TreeNode(temp.next.val)
            temp.next=None
            root.left=self.sortedListToBST(head)
            root.right=self.sortedListToBST(ans)
            return root
        elif length==1:
            root=TreeNode(head.val)
            return root
        return 
                
        
# @lc code=end

