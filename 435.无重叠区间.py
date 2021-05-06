#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        r=intervals[0][1]
        ans=1
        for i in intervals[1:]:
            if i[0]>=r:
                ans += 1
                r = i[1]
        return n-ans
# @lc code=end

