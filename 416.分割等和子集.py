#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if sum(nums)%2 or n<2:
            return False
        target=int(sum(nums)/2)
        dp=[True]+[False]*target
        for i ,num in enumerate(nums):
            for j in range(target,num-1,-1):
                dp[j]|=dp[j-num]
        return dp[target]

# @lc code=end

