#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m=len(flowerbed)
        for i in range(m):
            if flowerbed[i]==1:
                if i>0:
                    flowerbed[i-1]=2
                if i<m-1:
                    flowerbed[i+1]=2
        for i in range(m):
            if flowerbed[i]==0:
                if i<m-1:
                    flowerbed[i+1]=2 
        count=collections.Counter(flowerbed)[0]
        if count>=n:
            return True
        return False




# @lc code=end

