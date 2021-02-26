#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
import math
# @lc code=start
class Solution:
    def __init__(self):
        self.ans=''
    def getPermutation(self, n: int, k: int) -> str:
        if n==1:
            return '1'
        nums=[i for i in range(1,n+1)]
        self.digui(nums,n,k)
        return self.ans
    def digui(self,nums,n,k):
        if n>=1:
            nums=sorted(nums)
            count=math.factorial(n-1)
            div=int(k/count)
            mod=k%count
            if mod==0:
                self.ans+=str(nums[div-1])
                del nums[div-1]
            else:
                self.ans+=str(nums[div])
                del nums[div]
            self.digui(nums,n-1,mod)



# @lc code=end

