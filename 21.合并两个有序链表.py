#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        temp_head=head
        temp_l1=l1
        temp_l2=l2
        while temp_l1 or temp_l2:
            if temp_l1 and temp_l2:
                if temp_l1.val<=temp_l2.val:
                    temp_head.next=temp_l1
                    temp_head=temp_head.next
                    temp_l1=temp_l1.next
                else:
                    temp_head.next=temp_l2
                    temp_head=temp_head.next
                    temp_l2=temp_l2.next
            elif temp_l1:
                    temp_head.next=temp_l1
                    temp_head=temp_head.next
                    temp_l1=temp_l1.next
            elif temp_l2:
                    temp_head.next=temp_l2
                    temp_head=temp_head.next
                    temp_l2=temp_l2.next
        return head.next
                
# @lc code=end

