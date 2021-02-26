#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        temp_ans=ListNode()
        temp_r=ListNode()
        ans=temp_ans
        ans_r=temp_r
        temp=head
        while temp:
            if temp.val<x:
                temp_ans.next=temp
                temp_ans=temp_ans.next
            else:
                temp_r.next=temp
                temp_r=temp_r.next
            temp=temp.next
        temp_r.next=None
        temp_ans.next=ans_r.next
        return ans.next
            

# @lc code=end

