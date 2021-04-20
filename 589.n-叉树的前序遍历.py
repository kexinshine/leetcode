#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans=[]
        node_list=[]
        node_list.append(root)
        while node_list:
            node=node_list.pop(0)
            ans.append(node.val)
            for child in reversed(node.children):
                node_list.insert(0,child)
        return ans    



                
        
# @lc code=end

