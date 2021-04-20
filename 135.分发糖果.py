#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        l=list()
        l.append(1)
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                l.append(l[i-1]+1)
            else:
                l.append(1)
        r=[1]*n
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                r[i]=r[i+1]+1
        sum=0
        for i in range(n):
            sum+=max(l[i],r[i])
        return sum

            


# @lc code=end

