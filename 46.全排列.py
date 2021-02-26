#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=list()
        list1=list(itertools.permutations(nums,len(nums)))
        for i in list1:
            i=list(i)
            ans.append(i)
        return ans
# @lc code=end

