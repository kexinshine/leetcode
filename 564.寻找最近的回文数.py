#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#

# @lc code=start
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n)<10 or int(n[::-1])==1:
            return str(int(n)-1)
        if n=='11':
            return '9'
        if set(n)=={'9'}:
            return str(int(n)+2)
        a,b=n[:(len(n)+1)//2],n[(len(n)+1)//2:]
        temp=[str(int(a)-1),a,str(int(a)+1)]
        temp=[i+i[len(b)-1::-1] for i in temp]
        return min(temp,key=lambda x:abs(int(x)-int(n)) or float('inf'))

# @lc code=end

