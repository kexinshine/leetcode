/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = 0; 
        int maxlen = 0;
        for( ; r < s.size(); r++ ) {
            for( int k = l; k < r; k++ ) 
                if( s[r] == s[k] ) { 
                    l = k+1;
                    break; 
                }
            if(r-l+1 > maxlen)
                maxlen = r-l+1;     
            }
        return maxlen;
    }
};
// @lc code=end

