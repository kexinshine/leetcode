#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            hashmap = collections.defaultdict(int)
            for j in range(len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dis = dx * dx + dy * dy
                hashmap[dis] += 1
            for val in hashmap.values():
                    res += val * (val - 1)
        return res



# @lc code=end

