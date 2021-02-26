#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def div(self,b, a):                
        if b < a:
            return 0
        cur = a
        multiple = 1
        while cur + cur < b:             
            cur += cur                         
            multiple += multiple
        return multiple + self.div(b - cur, a)

    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647 
        flag = 1                                   
        if dividend < 0: 
            flag, dividend = -flag, -dividend
        if divisor < 0: 
            flag, divisor  = -flag, -divisor 
        res = self.div(dividend, divisor)
        res = res if flag > 0 else -res         
        if res < MIN_INT:                      
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT

# @lc code=end

