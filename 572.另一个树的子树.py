#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSametree(l,r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            elif l.val!=r.val:
                return False
            else:
                return isSametree(l.left,r.left) and isSametree(l.right,r.right)

        if not s and not t:
            return True
        elif not s and t:
            return False
        elif not t and s:
            return False
        elif s.val==t.val:
            return isSametree(s,t) or self.isSubtree(s.right,t) or self.isSubtree(s.left,t)
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
        
# @lc code=end

