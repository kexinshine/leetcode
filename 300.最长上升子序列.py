#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]
        for i in range(1,len(nums)):
            temp=1
            for j in range(len(dp)):
                if nums[i]>nums[j]:
                    temp=max(temp,dp[j]+1)
            dp.append(temp)
        return max(dp)

# @lc code=end

