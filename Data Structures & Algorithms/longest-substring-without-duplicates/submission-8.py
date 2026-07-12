class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        curr = []
        for i in range(len(s)):
            if s[i] in curr:
                dup_in_curr = curr.index(s[i])
                curr = curr[dup_in_curr+1:]
            
            curr.append(s[i])
            output = max(len(curr),output)
        return output