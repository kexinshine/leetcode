/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 */

// 动态规划
#include<string>
using namespace std;
// @lc code=start
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()){
            return s;
        }
        int len=s.size();
        int dp[1000][1000];
        memset(dp,0,sizeof(dp));
        int l=0,r=0;
        for(int i=len-2;i>=0;i--){
            dp[i][i]=1;
            for(int j=i+1;j<len;j++){
                dp[i][j]=(s[i]==s[j] && (j-i<3||dp[i+1][j-1]))?1:0;
                if(dp[i][j] && r-l<j-i){
                    l=i;
                    r=j;
                }
            }
        }
        return s.substr(l,r+1-l);
    }
};
// @lc code=end

