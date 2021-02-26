#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp=head
        if not temp:
            return head
        while temp.next:
            x=temp.val
            temp.val=temp.next.val
            temp.next.val=x
            temp=temp.next.next
            if not temp:
                break
        return head

# @lc code=end

