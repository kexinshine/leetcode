#
# @lc app=leetcode.cn id=587 lang=python3
#
# [587] 安装栅栏
#

# @lc code=start
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        ans=list()
        points.sort(key=lambda x:x[0])
        ans.append(points[0])
        if points[-1] not in ans:
            ans.append(points[-1])
        points.sort(key=lambda x:x[1])
        if points[0] not in ans:
            ans.append(points[0])
        if points[-1] not in ans:
            ans.append(points[-1])
        
        return ans




# @lc code=end

