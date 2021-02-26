#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            str_x=str(x)
            len_s=len(str_x)
            for i in range(int(len_s/2)):
                if str_x[i]!=str_x[len_s-i-1]:
                    return False
            return True


        
# @lc code=end

