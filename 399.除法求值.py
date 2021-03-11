#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        word_dict=collections.defaultdict(int)
        for i in range(len(equations)):
            a=equations[i][0]
            b=equations[i][1]
            keys=word_dict.keys()
            if a not in keys and b not in keys:
                word_dict[b]=1
                word_dict[a]=values[i]
            elif a not in keys:
                word_dict[a]=word_dict[b]*values[i]
            elif b not in keys:
                word_dict[b]=word_dict[a]/values[i]
        ans=list()
        for q in queries:
            a=word_dict.get(q[0])
            b=word_dict.get(q[1])
            if a and b:
                ans.append(a/b)
            else:
                ans.append(-1.0)
        return ans

# @lc code=end

