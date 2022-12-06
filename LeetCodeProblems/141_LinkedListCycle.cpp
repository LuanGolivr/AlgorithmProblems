#include <cstddef>

/*
    Time Complexity: O(N)
    Space Complexity: O(1)
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL){
            return false;
        }

        ListNode* slow = head;
        ListNode* fast = head;

        while(fast->next != NULL && fast->next->next != NULL){
            slow = slow->next;
            fast = fast->next->next;

            if(slow == fast){
                return true;
            }
        }

        return false;
    }
};