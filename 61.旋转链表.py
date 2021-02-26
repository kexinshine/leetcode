#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        temp=head
        len_list=1
        while temp.next:
            len_list+=1
            trail=temp.next
            temp=temp.next
        k=k%len_list
        while k>0:
            trail.next=head
            new_trail=head
            for i in range(len_list-2):
                new_trail=new_trail.next
            new_trail.next=None
            head=trail
            trail=new_trail
            k-=1
        return head
        
# @lc code=end

