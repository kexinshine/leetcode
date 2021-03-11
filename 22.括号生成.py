#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = list()
        for i in range(n):
            for l in self.generateParenthesis(i):
                for r in self.generateParenthesis(n-i-1):
                    ans.append(f'({l}){r}')
        return ans  
# @lc code=end

