#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        ans=[]
        for w in words:
            set4=set(w.lower())
            if set4 ==set4&set1 or set4 ==set4&set2 or set4 ==set4&set3:
                ans.append(w)
        return ans
# @lc code=end

