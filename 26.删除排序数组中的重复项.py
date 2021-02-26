#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        i=0
        while True:
            if len(nums)==i+1:
                return i+1
            if nums[i+1]==nums[i]:
                del nums[i+1]
            else:
                i+=1
# @lc code=end

