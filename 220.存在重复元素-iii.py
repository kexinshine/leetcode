#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False
        count=collections.defaultdict(list)
        for i in range(len(nums)):
            count[nums[i]].append(i)
        test_list=sorted(count.items(),key=lambda x:x[0])
        l=0
        r=0
        while True:
            if abs(test_list[r][0] - test_list[l][0]) <= t:
                for x in test_list[r][1]:
                    for y in test_list[l][1]:
                        if abs(x - y) <= k and x!=y:
                            return True
            if l == r and l == len(test_list) - 1:
                return False
            else:
                l += 1
                r = l
# @lc code=end

