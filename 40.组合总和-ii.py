#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        all=0
        for i in candidates:
            all+=i
        if all<target:
            return []
        ans = []
        temp = []
        def recursion(idx, res):
            print(temp)
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx + 1, res + candidates[idx]) 
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, 0)
        demo=[list(_) for _ in set([tuple(sorted(__)) for __ in ans])]
        return demo 
# @lc code=end

