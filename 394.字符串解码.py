#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack=list()
        ans=''
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
                continue
            temp=stack.pop()
            temp_s=''
            while temp!='[':
                temp_s=temp+temp_s
                temp=stack.pop()
            temp=stack.pop()
            num=''
            while True:
                num=temp+num
                if len(stack)>0:    
                    if stack[-1].isdigit():
                        temp=stack.pop()
                        continue
                    else:
                        break
                break
            num=int(num)
            stack.append(num*temp_s)
        for i in stack:
            ans+=i
        return ans
# @lc code=end

