#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[0])
        l,r=points[0][0],points[0][1]
        ans=1
        for ball in points[1:]:
            if ball[0]>r:
                ans+=1
                l=ball[0]
                r=ball[1]
            else:
                l=ball[0]
                r=min(r,ball[1])
        return ans


# @lc code=end

