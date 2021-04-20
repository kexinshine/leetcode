#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        word_dict={
            1:'A',
            2:'B',
            3:'C',
            4:'D',
            5:'E',
            6:'F',
            7:'G',
            8:'H',
            9:'I',
            10:'J',
            11:'K',
            12:'L',
            13:'M',
            14:'N',
            15:'O',
            16:'P',
            17:'Q',
            18:'R',
            19:'S',
            20:'T',
            21:'U',
            22:'V',
            23:'W',
            24:'X',
            25:'Y',
            26:'Z',       
        }
        ans=''
        div,mod=divmod(columnNumber,26)
        while div!=0:
            ans.append(word_dict.get(mod))
            div,mod=divmod(div,26)
        ans.append(word_dict.get(mod))
        return reversed(ans)

# @lc code=end

