#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        nums0 = nums.copy()
        for k in range(n):
            nums[k] = nums0[(n+1)//2-1-k//2] if (not k%2) else nums0[(n-1)-k//2]



# @lc code=end

