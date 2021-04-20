#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        end=timeSeries[0]
        ans=0
        for t in timeSeries:
            if t<end:
                ans-=(end-t)
            end=t+duration
            ans+=duration
        return ans 
# @lc code=end

