#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#

# @lc code=start
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n=len(routes)
        for i in range(n):
            if source in i and target in i:
                

# @lc code=end

