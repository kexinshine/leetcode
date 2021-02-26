#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        for i in range(len(nums) + 1):
            temp=set(itertools.combinations(nums, i))
            list_set = [list(_) for _ in set([tuple(sorted(__)) for __ in temp])]
            ans.append(list_set)

        res=list()
        for i in ans:
            for j in i:
                res.append(j)
        return res
# @lc code=end

