/*
 * @lc app=leetcode.cn id=6 lang=cpp
 *
 * [6] Z 字形变换
 */
#include<string>
using namespace std;
// @lc code=start
class Solution {
public:
string convert(string s, int numRows) {
        int len=s.size();
        string res;
        if(numRows==1){
            return s;
        }
        if(s.empty()){
            return s;
        }
        int j=0;
        int a[1000];
        int b[1000];
        for(int i=0;i<len;i+=2*numRows-2){
            a[j]=i;
            b[j]=i;
            j++;
        }
        int len_b=j;
        for(int i=1;i<numRows-1;i++){
            for(int n=0;b[n]+i<len&&n<len_b;n++){
                a[j]=b[n]+i;
                j++;
                if(b[n]+i+2*(numRows-1-i)<len){
                    a[j]=b[n]+i+2*(numRows-1-i);
                    j++;
                }
            }
        }
        for(int i=0;i<len_b;i++){
            if(b[i]+numRows-1<len){
                a[j]=b[i]+numRows-1;
                j++;
            }
        }
        for(int i=0;i<len;i++){
            res+=s[a[i]];
        }
        return res;
}
};
// @lc code=end

