#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        max_ans=0
        max_count=0
        for key,value in count.items():
            if value>max_count:
                max_ans=key
                max_count=value
        return max_ans
# @lc code=end

