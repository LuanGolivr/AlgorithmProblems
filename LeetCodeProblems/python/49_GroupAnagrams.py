import collections

class Solution:
    def groupAnagrams(self, strs):
        res = collections.defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            
            res[tuple(count)].append(word)
        
        return res.values()
    
    #TC = O(M * N)