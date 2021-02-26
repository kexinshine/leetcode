#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=list()
        list1=list(itertools.permutations(nums,len(nums)))
        for i in list1:
            i=list(i)
            if i not in ans:
                ans.append(i)
        return ans
# @lc code=end

