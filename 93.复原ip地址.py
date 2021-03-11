#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def __init__(self):
        self.ans=list()
    def restoreIpAddresses(self, s: str) -> List[str]:
        len_s=len(s)
        if len_s>12 or len_s<4:
            return []
        for n3 in range(3,len_s):
            for n2 in range(2,n3):
                for n1 in range(1,n2):
                    num_s=s[:n1]+'.'+s[n1:n2]+'.'+s[n2:n3]+'.'+s[n3:]
                    self.check(num_s)
        return self.ans
        
    def check(self,s):
        s_list=s.split('.')
        flag=1
        for num in s_list:
            if int(num)>255 or (len(num)>=2 and num.startswith('0')):
                flag=0
                break
        if flag:
            self.ans.append(s) 

# @lc code=end

