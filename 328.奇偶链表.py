#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        right=ListNode()
        temp_r=right
        cur=head
        while cur:
            temp=cur.next
            temp_r.next=temp
            temp_r=temp_r.next
            if temp:
                if not temp.next:
                    break
                cur.next=temp.next
                cur=temp.next
            else:
                break
        cur.next=right.next
        return head

# @lc code=end

