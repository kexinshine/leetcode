#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count=dict()
        for p in prerequisites:
            if p[1] not in count.keys():
                count[p[1]]=[p[0]]
                continue
            count[p[1]].append(p[0])
        
# @lc code=end

