class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        for i in s:
            s_hashmap[i] = s_hashmap.get(i, 0) +1
        
        for j in t:
            t_hashmap[j] = t_hashmap.get(j, 0) +1

        return s_hashmap == t_hashmap