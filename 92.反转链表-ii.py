#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:
            return head
        temp=head
        ans1=ListNode()
        ans1_res=ListNode()
        ans1_res.next=ans1
        count=1
        while count<=right:
            print(temp.val)
            if count==left:
                ans2=ListNode(temp.val)
                ans3=ans2
            elif count>left:
                ans2_temp=ListNode(temp.val)
                ans2_temp.next=ans2
                ans2=ans2_temp
            else:
                ans1_temp=ListNode(temp.val)
                ans1.next=ans1_temp
                ans1=ans1.next
            temp=temp.next
            count+=1
        ans1.next=ans2
        ans3.next=temp
        return ans1_res.next.next
# @lc code=end

