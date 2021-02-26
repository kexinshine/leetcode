#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if set(p) == {"*"}: return True
        zong = len(p)+1 
        heng = len(s)+1 
        table = [[False]*heng for i in range(zong)]
        table[0][0] = True
        if p.startswith("*"):
            table[1] = [True]*heng
        for m in range(1,zong):
            path = False 
            for n in range(1,heng):
                if p[m-1] == "*": 
                    if table[m-1][0] == True:
                        table[m] = [True]*heng
                    if table[m-1][n]: 
                        path = True
                    if path:
                        table[m][n] = True
                elif p[m-1] == "?" or p[m-1]==s[n-1]:
                    table[m][n] = table[m-1][n-1] 
                    
        return table[zong-1][heng-1]
# @lc code=end

