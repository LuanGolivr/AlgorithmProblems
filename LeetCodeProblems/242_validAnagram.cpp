#include <unordered_map>
#include <string>
#include <string.h>

/*

    Time Complexity: O(N) because we're going to itarate through the lenght of one of strings
    Space Complecity: O(1) because since we're using an array to store the number of letter on the strings and we've got 26 letters in our alphabet so it is O(26) but 26 become a constant so it is O(1)

*/


class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if(s.size() != t.size()){
            return false;
        }

        int counts[26] = {0};

        for(int i = 0; i < s.size(); i++){
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }

        for(int j = 0; j < 26; j++){
            if(counts[j]) return false;
        }

        return true;
    }
};