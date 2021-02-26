#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums=len(nums)
        l=0
        r=1
        count=1
        while r<len_nums:
            if nums[r]==nums[l]:
                count+=1
            elif nums[r]!=nums[l]:
                l=r
                count=1
            if count > 2 :
                nums[r]=10001
                count-=1
            r+=1
        while 10001 in nums:
            nums.remove(10001)
        return len(nums)
            

# @lc code=end

