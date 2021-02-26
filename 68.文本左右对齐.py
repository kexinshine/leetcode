#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp=''
        ans=list()
        for word  in words:
            res=temp
            temp+=word
            if len(temp)<maxWidth:
                temp+=' '
            elif len(temp)==maxWidth:
                ans.append(temp)
                res=''
                temp=''
            else:
                ans.append(res)
                res=''
                temp=word+' '
        ans.append(temp)
        if ans[-1]=='':
            ans=ans[:-1]
        res=list()
        for s in ans:
            s_list=s.split(' ')
            if ans.index(s)==len(ans)-1:
                temp_str=''
                for i in s_list:
                    temp_str+=i+' '
                if len(temp_str)>maxWidth:
                    temp_str=temp_str[:maxWidth]
                while len(temp_str)<maxWidth:
                    temp_str+=' '
                res.append(temp_str)
                break
            if s_list[-1]=='':
                temp_str=''
                s_list=s_list[:-1]
                count=len(s_list)
                if count==1:
                    res.append(s_list[0]+(maxWidth-len(s_list[0]))*' ')
                    continue
                length=0
                for demo in s_list:
                    length+=len(demo)
                div=int((maxWidth-length)/(count-1))
                mod=(maxWidth-length)%(count-1)
                for i in range(count):
                    if i==count-1:
                        temp_str+=s_list[i]
                        break
                    if mod>0:
                        temp_str+=s_list[i]+div*' '+' '
                        mod-=1
                    else:
                        temp_str+=s_list[i]+div*' '
                res.append(temp_str)
            else:
                res.append(s)
        return res

# @lc code=end

