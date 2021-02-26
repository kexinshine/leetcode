#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_d=len(digits)
        reversed_list=list(reversed(digits))
        reversed_list[0]+=1
        for i in range(len_d):
            if reversed_list[i] <=9:
                break
            else:
                reversed_list[i]=0
                if i ==len_d-1:
                    reversed_list.append(1)
                else:
                    reversed_list[i+1]+=1
        return list(reversed(reversed_list))
# @lc code=end

