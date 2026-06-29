class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i],0)+1
        
        for j in range(len(t)):
            t_hashmap[t[j]] = t_hashmap.get(t[j],0)+1
        
        return s_hashmap == t_hashmap