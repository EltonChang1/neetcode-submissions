class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for ind, char in enumerate(s):
            s_hash[char] = s_hash.get(char, 0)+1

        for ind, char in enumerate(t):
            t_hash[char] = t_hash.get(char, 0)+1
        
        return s_hash == t_hash
