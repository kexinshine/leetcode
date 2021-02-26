#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        link=ListNode()
        ans=ListNode()
        ans.next=link
        l=head
        r=head
        count=1
        while r.next:
            temp=r.next
            print(l.val,temp.val,count)
            if temp.val==l.val:
                count+=1
                r=temp
                continue
            if count<=1:
                print(f'拼接{l.val}')
                temp_node=ListNode()
                temp_node.val=l.val
                link.next=temp_node
                link=link.next
                count=1
                l=temp
                r=temp
            else:
                l=temp
                r=temp
                count=1
        if count==1:
            link.next=temp
        return ans.next.next
# @lc code=end

