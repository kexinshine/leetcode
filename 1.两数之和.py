#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                a = target - nums[i]
                for j in range(i + 1, len(nums)):
                    if a == nums[j]:
                        return [i, j]
# @lc code=end

