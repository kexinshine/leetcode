#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = list(num1)[-1::-1]
        num2 = list(num2)[-1::-1]
        self.res = [0 for i in range(len(num1) + len(num2) + 1)]
        for i,x in enumerate(num1):
            for j,y in enumerate(num2):
                _t = int(x) * int(y)
                self.add_ij_in_position(i+j, _t)
        while self.res[-1] == 0:
            self.res.pop()
            if not self.res:
                return '0'
        self.res.reverse()
        return "".join((str(x) for x in self.res))

    def add_ij_in_position(self, ij, num):
        new = self.res[ij+1]*10 + self.res[ij] + num
        self.res[ij] = new % 10
        self.res[ij + 1] = new // 10 % 10
        if new // 100:
            self.res[ij + 2] = self.res[ij + 2] + new // 100
# @lc code=end

