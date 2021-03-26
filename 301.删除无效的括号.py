#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            stack=list()
            for i in s:
                if i=='(':
                    stack.append('(')
                elif i==')':
                    if not stack:
                        return False
                    if stack[-1]!='(':
                        return False
                    stack.pop()
                else:
                    continue
            if not stack:
                return True
            return False
        start=[s]
        while True:
            res=list(filter(isvalid,list(start)))
            if res:
                return res
            nex=set()
            for i in start:
                for j in range(len(i)):
                    nex.add(i[:j]+i[j+1:len(i)])
            start=nex
        



# @lc code=end

