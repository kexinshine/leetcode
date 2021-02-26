#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=list()
        for i in range(len(nums)+1):
            per_list=itertools.combinations(nums,i)
            for per in per_list:
                temp_list = list()
                for p in per:
                    temp_list.append(int(p))
                ans.append(temp_list)
        return ans
# @lc code=end

