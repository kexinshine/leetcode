#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def bit_sqrt(n):
            sum=0
            while n>0:
                temp=n%10
                sum+=temp**2
                n/=10
            return sum

        slow=bit_sqrt(n)
        fast=bit_sqrt(bit_sqrt(n))
        while slow !=fast:
            slow=bit_sqrt(slow)
            fast=bit_sqrt(bit_sqrt(fast))
        return slow==1
# @lc code=end

