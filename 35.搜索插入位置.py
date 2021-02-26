#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums=len(nums)
        if target<nums[0]:
            return 0
        if target>nums[len_nums-1]:
            return len_nums
        l=0
        r=len_nums-1
        m=int((l+r)/2)
        temp=0
        while True:
            if nums[m]<target:
                l=m
                m=ceil((l+r)/2)
            elif nums[m]>target:
                r=m
                m=floor((l+r)/2)
            else:
                return m
            if l==m and m==r:
                break
            elif l==m and m==r-1:
                if temp==0:
                    temp+=1
                else:
                    break
        return l+1

# @lc code=end

