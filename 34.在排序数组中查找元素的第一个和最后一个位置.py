#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_nums=len(nums)
        if len_nums==0:
            return [-1,-1]
        m=int(len_nums/2)
        l=0
        r=len_nums-1
        flag=0
        temp=0
        while True:
            print(l,m,r)
            if nums[m]<target:
                l=m
                m=ceil((l+r)/2)
            elif nums[m]>target:
                r=m
                m=floor((l+r)/2)
            else:
                flag=1
                break
            if l==m and m==r:
                break
            elif l==m and m==r-1:
                if temp==0:
                    temp+=1
                else:
                    break
        if flag:
            l=m
            r=m
            while l>0:
                if nums[l-1]==target:
                    l-=1
                else:
                    break
            while r<len_nums-1:
                if nums[r+1]==target:
                    r+=1
                else:
                    break
            return [l,r]
        return [-1,-1]
# @lc code=end

