#
# @lc app=leetcode.cn id=335 lang=python3
#
# [335] 路径交叉
#

# @lc code=start
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        if distance[2]>distance[0]:
            return False
        elif distance[2]<distance[0] and distance[3]<distance[1]:
            return False
        return True

# @lc code=end

