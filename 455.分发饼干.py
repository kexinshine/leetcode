#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        for i in s:
            if g and i>=g[0]:
                del g[0]
                ans+=1
            elif not g:
                break
        return ans
# @lc code=end

