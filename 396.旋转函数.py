#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = 0
        length = len(nums)
        for i in range(length):
            f += i*nums[i]
        maxf = f
        ss = sum(nums)
        for i in range(length-1,-1,-1):
            f = f - (length-1)*nums[i] + ss - nums[i]
            maxf = max(f,maxf)
        return maxf

# @lc code=end

