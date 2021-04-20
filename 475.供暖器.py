#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans=[]
        houses.sort()
        heaters.sort()
        n_houses=len(houses)
        n_heaters=len(heaters)
        for house in houses:
            i=bisect.bisect(heaters,house)
            if i==0:
                ans.append(abs(heaters[0]-house))
            elif i==n_heaters:
                ans.append(abs(heaters[-1]-house))
            else:
                ans.append(min(abs(heaters[i-1]-house),abs(heaters[i]-house)))
        return max(ans)
# @lc code=end

