#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        if root.left and root.right:
            root.left.next=root.right
            temp=root.next
            while temp:
                if temp.left:
                    root.right.next=temp.left
                    break
                elif temp.right:
                    root.right.next=temp.right
                    break
                temp=temp.next
            self.connect(root.right)
            self.connect(root.left)
        elif root.left:
            temp=root.next
            while temp:
                if temp.left:
                    root.left.next=temp.left
                    break
                elif temp.right:
                    root.left.next=temp.right
                    break
                temp=temp.next
            self.connect(root.left)
        elif root.right:
            temp=root.next
            while temp:
                if temp.left:
                    root.right.next=temp.left
                    break
                elif temp.right:
                    root.right.next=temp.right
                    break
                temp=temp.next
            self.connect(root.right)
        return root
        
# @lc code=end

