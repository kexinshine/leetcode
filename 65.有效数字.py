#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        def isallnumber(in_str):
            print(in_str)
            if in_str[0]=='+' or in_str=='-':
                if len(in_str)==1:
                    return False
                in_str=in_str[1:]
            for i in in_str:
                if ord(i)>57:
                    return False
            return True
        head=['-','+','.','0','1','2','3','4','5','6','7','8','9']
        if s[0] not in head:
            return False
        map=collections.defaultdict(int)
        map['.']=map['-']=map['+']=map['e']=map['E']=0
        for i in range(10):
            map[f'{i}']=0
        for i in s:
            if (ord(i)>=65 and ord(i)<=68) or (ord(i)>=70 and ord(i)<=90) \
            or (ord(i)>=97 and ord(i)<=100) or (ord(i)>=102 and ord(i)<=122):
                return False
            map[i]+=1
        if map['.']>1 or map['-']>1 or map['+']>2 or (map['e']+map['E'])>1:
            return False
        if map['-']==1 and s.index('-')!=0:
            if map['e']==1:
                if s.index('-')-1!=s.index('e'):
                    return False
            else:
                return False
        if map['+']==1 and s.index('+')!=0:
            if map['e']==1:
                if s.index('+')-1!=s.index('e'):
                    return False
            else:
                return False
        if map['.']==1 and map['e']==0 and map['E']==0:
            s_list=s.split('.')
            if '-'  in s_list[0] or '+' in s_list[0]:
                s_list[0]=s_list[0][1:]
            if s_list[0]=='' and s_list[1]=='':
                return False
        if map['.']==1 and (map['e']==1 or map['E']==1):
            if map['e']==1:
                s_list=s.split('e')
                if s.index('e')<s.index('.'):
                    return False
            if map['E']==1:
                s_list=s.split('E')  
                if s.index('E')<s.index('.'):
                    return False
            if s_list[1]=='':
                return False  
            if not isallnumber(s_list[1]):
                return False
            if '-'  in s_list[0] or '+' in s_list[0]:
                s_list[0]=s_list[0][1:]
            temp_list=s_list[0].split('.')
            if temp_list[0]=='' and temp_list[1]=='':
                return False
        if map['.']==0 and (map['e']==1 or map['E']==1):
            if map['e']==1:
                s_list=s.split('e')
            if map['E']==1:
                s_list=s.split('E')      
            if s_list[1]=='':
                return False
            if not isallnumber(s_list[1]):
                return False
            if '-'  in s_list[0] or '+' in s_list[0]:
                s_list[0]=s_list[0][1:]
            if len(s_list[0])<1:
                return False
        if map['.']==0 and map['e']==0 and map['E']==0:
            if '-' in s or '+' in s:
                s=s[1:]
            if not isallnumber(s):
                return False
        return True
# @lc code=end

