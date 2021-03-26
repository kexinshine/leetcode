#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        d=[0]*n
        for i in nums:
            d[i]+=1
            if d[i]>1:
                return i
# @lc code=end

