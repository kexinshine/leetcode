#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        lens = len(s)
        sums = 0
        i = 0
        while i < lens:
            j = i+1
            if j < lens and dic[s[i]] < dic[s[j]] :#左边的数是否小于右边的数
                sums += dic[s[j]] - dic[s[i]]
                i += 2
            else :
                sums += dic[s[i]]
                i += 1
        return sums



# @lc code=end

