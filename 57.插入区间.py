#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        len_int=len(intervals)
        sort_list=sorted(intervals,key=lambda temp:temp[0])
        ans=list()
        ans.append(sort_list[0])
        len_ans=1
        for i in range(1,len_int):
            if sort_list[i][0]<=ans[len_ans-1][1]:
                ans[len_ans-1][1]=max(sort_list[i][1],ans[len_ans-1][1])
            else:
                ans.append(sort_list[i])
                len_ans+=1
        return ans
# @lc code=end

