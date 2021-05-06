#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:   return False        

        from sortedcontainers import SortedList
        window = SortedList()

        for i,num in enumerate(nums):
            idx = window.bisect_left(num - t)   #第一个 >= (num-t)的index
            if idx < len(window) and window[idx] <= (num + t):
                return True

            window.add(num)                     #进R
            if i >= k:                          #弹L
                window.remove(nums[i-k])

        return False
# @lc code=end

