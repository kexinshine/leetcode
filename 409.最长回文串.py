#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        count_list=list(count.values())
        ans=sum(count_list)
        for i in range(len(count_list)):
            if count_list[i]%2!=0:
                ans-=1
        return ans+1 if ans!=sum(count_list) else ans
            
# @lc code=end

