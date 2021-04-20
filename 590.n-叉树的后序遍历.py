#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans=[]
        node_list=[]
        node_list.append(root)
        while node_list:
            node=node_list.pop(-1)
            ans.insert(0,node.val)
            for child in node.children:
                node_list.append(child)
        return ans    
        
# @lc code=end

