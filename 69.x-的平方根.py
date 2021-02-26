#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        l=0
        r=x
        while True:
            ans=int((l+r)/2)
            if pow(ans,2)==x:
                return ans
            elif pow(ans,2)<x:
                if pow(ans+1,2)>x:
                    return ans
                l=(l+r)/2
            elif pow(ans,2)>x:
                if pow(ans-1,2)<x:
                    return ans-1
                r=(l+r)/2

            
# @lc code=end

