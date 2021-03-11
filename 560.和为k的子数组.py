#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        occur = {0: 1}
        res = 0
        s = 0
        for num in nums:
            s += num
            temp = occur.get(s-k, 0)
            res += temp
            occur[s] = occur.get(s, 0) + 1
        return res
# @lc code=end

