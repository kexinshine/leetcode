#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count=[]
        for st in strs:
            count_0=count_1=0
            for s in st:
                if s=='0':
                    count_0+=1
                else:
                    count_1+=1
            count.append((count_0,count_1))
        print(count)
# @lc code=end

