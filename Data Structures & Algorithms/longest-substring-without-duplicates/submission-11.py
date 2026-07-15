class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        left = 0 
        hashset = set()

        for i in range(len(s)):
            if s[i] in hashset:
                while s[i] in hashset:
                    hashset.remove(s[left])
                    left += 1
            hashset.add(s[i])
            output = max(output, len(hashset))
        
        return output

            
