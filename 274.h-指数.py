#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        if n==0 or citations[-1]==0:
            return 0
        for i in range(n):
            if citations[i]>=n-i:
                return n-i 


# @lc code=end

