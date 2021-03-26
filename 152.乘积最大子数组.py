#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp_min=dp_max=ans=nums[0]
        for i in range(1,n):
            dp_max,dp_min=max(nums[i],dp_max*nums[i],dp_min*nums[i]),min(nums[i],dp_max*nums[i],dp_min*nums[i])
            ans=max(dp_max,ans)        
        return ans
# @lc code=end

