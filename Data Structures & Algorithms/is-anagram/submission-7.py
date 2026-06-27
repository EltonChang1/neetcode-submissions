class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        for i in s:
            if i not in s_hashmap:
                s_hashmap[i] = s_hashmap.get(i, 0) + 1
            else:
                s_hashmap[i] += 1
        
        for j in t:
            if j not in t_hashmap:
                t_hashmap[j] = t_hashmap.get(j , 0) +1
            else:
                t_hashmap[j] += 1

        return s_hashmap == t_hashmap
                
            
        