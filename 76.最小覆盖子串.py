#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self,s: str, t: str) -> str:
        def check(dict1, dict2):
            for key, value in dict2.items():
                if dict1[key] < value:
                    return False
            return True
        len_s = len(s)
        len_t = len(t)
        if len_s < len_t:
            return ''
        l = 0
        r = 0
        ans = dict()
        map_t = dict()
        res = list()
        for i in t:
            map_t.setdefault(i, 0)
            ans.setdefault(i, 0)
            map_t[i] += 1
        while r < len_s:
            flag=0
            for i in s[r:]:
                r += 1
                ans.setdefault(i, 0)
                ans[i] += 1
                if check(ans, map_t):
                    flag=1
                    break
            if flag==0:
                break
            for i in s[l:r]:
                l += 1
                ans[i] -= 1
                if not check(ans, map_t):
                    ans[i]+=1
                    res.append(s[l - 1:r])
                    break
            ans[s[l-1]] -= 1
        if not res:
            return ''
        return sorted(res,key=lambda x:len(x))[0]



# @lc code=end

