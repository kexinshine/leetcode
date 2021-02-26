#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        same_pre=''
        same_index=0
        flag=True
        min_len=999
        for str_temp in strs:
            min_len=min_len if len(str_temp)>min_len else len(str_temp)
        if not strs:
            return ''
        while True:
            if same_index<min_len:
                temp_str=strs[0][same_index]
                for str_demo in strs:
                    if str_demo[same_index]!=temp_str:
                        flag=False
                        break
                if flag:
                    same_pre+=temp_str
                    same_index+=1
                else:
                    return same_pre
            else:
                return same_pre
# @lc code=end

