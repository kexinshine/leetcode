#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(filter(str.isalnum,s)).lower()
        len_s=len(s)
        if len_s==0:
            return True
        l=0
        r=len_s-1
        while l<=r-1:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
# @lc code=end

