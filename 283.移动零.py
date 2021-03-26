#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        end=len(nums)
        while start<end:
            if not nums[start]:
                del nums[start]
                nums.append(0)
                end-=1
            else:
                start+=1
# @lc code=end

