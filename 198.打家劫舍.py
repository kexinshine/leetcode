#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[nums[0],max(nums[1],nums[0])]
        for i in range(2,n):
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))
        return dp[n-1]


# @lc code=end

