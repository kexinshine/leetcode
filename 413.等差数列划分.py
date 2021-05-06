#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        #计数
        count = 0
        for i in range(1, len(nums)):
            #每两个相连位置的差值
            d = nums[i] - nums[i - 1]
            #往当前索引向后遍历
            for j in range(i + 1, len(nums)):
                #如果是连续等差值则加入
                if nums[j] - nums[j - 1] == d:
                    count += 1
                #否则退出
                else:
                    break
        return count



# @lc code=end

