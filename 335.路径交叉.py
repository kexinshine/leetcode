#
# @lc app=leetcode.cn id=335 lang=python3
#
# [335] 路径交叉
#

# @lc code=start
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        if len(x) <  4:return False
        if len(x) == 4:return True if x[3] >= x[1] and x[2] <= x[0] else False
        for i in range(3, len(x)):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            if i > 3 and x[i-1] == x[i-3] and x[i-4] + x[i] >= x[i-2]:
                return True
            if i > 4 and x[i-3]-x[i-5] <= x[i-1] <= x[i-3] and x[i-2]-x[i-4] <= x[i] <= x[i-2] and x[i-2] > x[i-4]:
                return True
        return False

# @lc code=end

