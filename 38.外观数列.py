#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#
from itertools import groupby
# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        self.dp()
        return self.res[n]
        
    def dp(self):
        self.res = list()
        self.res.append('1')
        self.res.append('1')
        for i in range(31):
            if i > 1:
                self.res.append('')
                temp = [''.join(g) for _, g in groupby(self.res[i - 1])]
                for group in temp:
                    self.res[i] += (str(len(group)) + group[0])


    
# @lc code=end

