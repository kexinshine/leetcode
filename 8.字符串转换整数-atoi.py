#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s:str)->int:
        s=s.strip('\"')
        s=s.lstrip()
        res=0
        if len(s)==0:
            return 0
        if (ord(s[0])>=48  and ord(s[0])<=57):
            for char in s:
                if (ord(char)>=48  and ord(char)<=57):
                    res=int(char)+res*10
                else:
                    break
            if res>2**31-1:
                return 2**31-1
            else:
                return res
        elif s[0]=='-' or s[0]=='+':
            print(s)
            for char in s[1:]:
                print(char)
                if (ord(char)>=48  and ord(char)<=57):
                    res=int(char)+res*10
                else:
                    break
            print(res)
            if s[0]=='-':
                res=res*(-1)
            if res<-2**31:
                return -2**31
            elif res>2**31-1:
                return 2**31-1
            else:
                return res
        else:
            return 0

# @lc code=end

