#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            pattern=re.compile(p)
            res=pattern.search(s)
            if res:
                if res.group()==s:
                    return True
                else:
                    return False
            else:
                return False




# @lc code=end

