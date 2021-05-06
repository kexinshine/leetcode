#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        ans=0
        while n>=i:
            n-=i
            i+=1
            ans+=1
        return ans
# @lc code=end

