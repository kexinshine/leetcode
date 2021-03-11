#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp=[]
        dp.append({
            nums[0]:1,
            -nums[0]:1
        })
        if nums[0]==0:
            dp=[{
                0:2
            }]
        n=len(nums)
        for i in range(1,n):
            temp=collections.defaultdict(int)
            for key,value in dp[i-1].items():
                temp[nums[i]+key]+=value
                temp[-nums[i]+key]+=value
            dp.append(temp)       
        try:
            return dp[n-1][S]
        except:
            return 0
# @lc code=end

