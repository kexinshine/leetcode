#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0') or '00' in s:
            return 0
        len_s=len(s)
        if len_s==1:
            return 1
        dp=list()
        dp.append(1)
        if int(s[:2])<=26 and s[1]!='0':
            dp.append(2)
        elif s[1]=='0' and int(s[:2])>26:
            return 0
        else:
            dp.append(1)
        for i in range(2, len_s):
            if int(s[i - 1:i + 1]) == 0 or (s[i]=='0' and int(s[i - 1:i + 1])>26):
                return 0
            elif s[i] == '0':
                dp.append(dp[i - 2])
            elif s[i - 1] == '0' or int(s[i - 1:i + 1])>26:
                dp.append(dp[i - 1])
            else:
                dp.append(dp[i - 1] + dp[i - 2])
        return dp[len_s-1]
# @lc code=end

