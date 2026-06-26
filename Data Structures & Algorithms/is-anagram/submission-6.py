class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_h = {}
        t_h = {}

        for i in range(len(s)):
            if s[i] not in s_h:
                s_h[s[i]] = 1
            else:
                s_h[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in t_h:
                t_h[t[j]] = 1
            else:
                t_h[t[j]] += 1

        return s_h == t_h
                
            
        