#include <string>

/*
    Time complexity: O(N) because we're going to iterate through every single element on the string only once.
    Space complexity: O(1) we're not storing anything.
*/


class Solution {
public:
    bool isPalindrome(std::string s) {
        int i = 0;
        int j = s.size() - 1;
        
        while (i < j) {
            while (!isalnum(s[i]) && i < j) {
                i++;
            }
            while (!isalnum(s[j]) && i < j) {
                j--;
            }
            if (tolower(s[i]) != tolower(s[j])) {
                return false;
            }
            i++;
            j--;
        }
        
        return true;
    }
};