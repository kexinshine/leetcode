#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count=collections.defaultdict(list)
        for i in range(len(nums)):
            count[nums[i]].append(i)
        test_list=[v for v in count.values() if len(v)>1]
        for t in test_list:
            for i in range(1,len(t)):
                if t[i]-t[i-1]<=k:
                    return True
        return False


# @lc code=end

