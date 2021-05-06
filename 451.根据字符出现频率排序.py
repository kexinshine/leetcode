#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        count=collections.Counter(s)
        ans=''
        l=[]
        for key,value in count.items():
            l.append((key,value))
        l.sort(key=lambda x:-x[1])
        for i in l:
            ans+=i[0]*i[1]
        return ans
# @lc code=end

