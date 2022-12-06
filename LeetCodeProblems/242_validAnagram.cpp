#include <unordered_map>
#include <string>
#include <string.h>

/*

    Time Complexity: O(N + M) because we're going to itarate through the each string only once
    Space Complecity: O(N) because we're going to store the letters of one the strings to compare to the other string

*/


class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if(s.size() != t.size()){
            return false;
        }

        std::unordered_map<char, int> cachingS;
        
        for(int i = 0; i < s.size(); i++){
            if(cachingS.find(s[i]) != cachingS.end()){
                cachingS[s[i]] += 1;
            }else {
                cachingS.insert({s[i], 1});
            }
        }

        for(int j = 0; j < t.size(); j++){
            if(cachingS.find(t[j]) != cachingS.end()){
                cachingS[t[j]] -= 1;

                if(cachingS[t[j]] <= -1){
                    return false;
                }
            }else {
                return false;
            }
        }

        return true;
    }
};