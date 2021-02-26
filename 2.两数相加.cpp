class Solution {
    int flag=0;
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l2||l1){
            int res=l1->val+l2->val+flag;
            if(res>=10){
                l1->val=res%10;
                flag=1;
            }
            else{
                l1->val=res;
                flag=0;
            }
            if(!l1->next && l2->next){
                l1->next=new struct ListNode(0);
                addTwoNumbers(l1->next,l2->next);
            }
            else if(l1->next && !l2->next){
                l2->next=new struct ListNode(0);
                addTwoNumbers(l1->next,l2->next);
            }
            else if(l1->next && l2->next){
                addTwoNumbers(l1->next,l2->next);
            }
            else{
                if(flag){
                    l1->next=new struct ListNode(1);
                    return l1;
                }
            }
        }
        return l1;
    }
};

// @lc code=end

