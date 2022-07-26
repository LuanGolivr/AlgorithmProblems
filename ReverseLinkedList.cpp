#include <iostream>

using namespace std;

int main(){
    
    //Definition for singly-linked list.
    struct ListNode {
        int val;
        ListNode *next;
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };

    // Basicly what we gonna do is use two pointer to switch the connections without losing the next's
    //values

    ListNode* prevNode = NULL;
    ListNode* currNode = head;// The "head" over here means the first Node of the linkedList, for example. if the linked-list was 1 -> 2 -> 3 -> 4 -> 5 , the head would be the Node 1.
    ListNode* nxt ;

    while (currNode){
        nxt = currNode->next;
        currNode->next = prevNode;
        prevNode = currNode;
        currNode = nxt;
    }
    // Using the iterative solution you've got a : O(n) Time Complexity and O(1) Space Complexity 
    // The alghoritmn above represents the iterative approach, lets try the recursive approach now right


    void recursive(ListNode* head){
        if (head == NULL){
            return NULL;
        }

        ListNode* newHead = head;
        if(head -> next){
            newHead = recursive(head->next);
            head->next->next = head;
        }
        head->next = NULL;
        return newHead;
    };

    //Time Complexity: O(n)
    //Space Complexity: O(n)

    
    
    return 0;
}