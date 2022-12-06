#include <stack>
#include <string>

/*
    Time complexity: O(N) because we're just visiting each element of the string once.
    Space complexity: O(N) because we're going to store every single element of the string on the stack.

*/


class Solution {
public:
    bool isValid(std::string s) {
        std::stack<int> stck;

        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(' || s[i] == '{' || s[i] == '['){
                stck.push(s[i]);
                
            }else if(s[i] == ')' && !stck.empty() && stck.top() == '('){
                stck.pop();
            }else if(s[i] == '}' && !stck.empty() && stck.top() == '{'){
                stck.pop();
            }else if(s[i] == ']' && !stck.empty() && stck.top() == '['){
                stck.pop();
            }else {
                return false;
            }
        }

        if(stck.size() > 0){
            return false;
        }

        return true;
    }
};