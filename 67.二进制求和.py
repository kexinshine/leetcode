#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rev_a=a[::-1]
        rev_b=b[::-1]
        ans=''
        len_a=len(a)
        len_b=len(b)
        i=j=0
        flag=0
        while i<len_a or j<len_b:
            if i>=len_a:
                temp=int(rev_b[j])+flag
                if temp>1:
                    ans+='0'
                    j+=1
                    continue
                flag=0
                ans+=str(temp)
                j+=1
                continue
            if j>=len_b:
                temp=int(rev_a[i])+flag
                if temp>1:
                    ans+='0'
                    i+=1
                    continue
                flag=0
                ans+=str(temp)
                i+=1
                continue
            temp=int(rev_a[i])+int(rev_b[j])+flag
            if temp==2:
                ans+='0'
                flag=1
            elif temp==3:
                ans+='1'
                flag=1
            else:
                ans+=f'{temp}'
                flag=0
            i+=1
            j+=1 
        if flag:
            ans+='1'
        return ans[::-1]
# @lc code=end

