#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l=headA
        r=headB
        while True:
            if l==r:
                return l
            if l!=r and l.next and r.next:
                l=l.next
                r=r.next
            elif l!=r and not l.next and not r.next:
                return
            elif l!=r and not l.next:
                l=headB
                r=r.next
            elif l!=r and not r.next:
                r=headA
                l=l.next


        
            
# @lc code=end

