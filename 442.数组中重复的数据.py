#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                ans.append(abs(nums[i]))
            nums[abs(nums[i])-1]=-nums[abs(nums[i])-1]
        return ans
# @lc code=end

