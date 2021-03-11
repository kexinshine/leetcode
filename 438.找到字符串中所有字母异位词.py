#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p=collections.Counter(p)
        ans=list()
        for i in range(len(s)-len(p)+1):
            if collections.Counter(s[i:i+len(p)])==count_p:
                ans.append(i)
        return ans
# @lc code=end

