

import collections 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ht1 = collections.defaultdict(int)
        ht2 = collections.defaultdict(int)
        for l in s:
            ht1[l] += 1
            
        for l in t:
            ht2[l] += 1
            
        for k, v in ht1.items():
            if k not in ht2 or ht2[k] != v:
                return False
            
        
        return True
      
      
     '''JS SOLUTION:
     var isAnagram = function(s, t) {
    if (s.length === 1){
        return s===t;
    }
    if (s.length !== t.length){
        return false;
    }
    
    var charMap = new Map(); 
    
    for (let i = 0; i < s.length;i++){
        if (charMap[s.charCodeAt(i)]){
            charMap[s.charCodeAt(i)] += 1;
        }else{
            charMap[s.charCodeAt(i)] = 1;
        }
    }
    
    for (let j = 0; j < t.length;j++){
        if (charMap[t.charCodeAt(j)]){
            charMap[t.charCodeAt(j)] -= 1;
        } else{
            return false;
        }
    }
    
    for (const c of charMap.values()){
        if (c > 0){
            return false;
        }
    }
    
    return true;
    
    
};
'''
