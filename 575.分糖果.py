#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        count = Counter(candyType)
        len_key=len(count.keys())
        if len_key>=n/2:
            return int(n/2)
        else:
            return len_key

# @lc code=end

