#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        len_node=1
        temp_head=head
        while temp_head.next:
            len_node+=1
            temp_head=temp_head.next
        index_from_start=len_node-n+1
        if index_from_start<2:
            return head.next
        temp_left=head
        for i in range(index_from_start-2):
            temp_left=temp_left.next
        temp_right=temp_left.next.next
        temp_left.next=temp_right
        return head

        
# @lc code=end

