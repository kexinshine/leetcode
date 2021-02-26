#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums=len(nums)
        dp=[nums[0]]
        ans=nums[0]
        for i in range(1,len_nums):
            dp.append(max(dp[i-1]+nums[i],nums[i]))
            ans=max(ans,dp[i])
        return ans

# @lc code=end

