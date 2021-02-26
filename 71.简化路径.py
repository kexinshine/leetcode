#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list=path.split('/')
        path_stack=list()
        for e in path_list:
            if e=='..':
                if len(path_stack)>0:
                    path_stack.pop()
            elif e!='.' and e!='':
                path_stack.append(e)
        ans='/'
        ans+='/'.join(path_stack)
        return ans

# @lc code=end

