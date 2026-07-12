class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        curr = set()
        curr_left = 0
        for i in range(len(s)):
            while s[i] in curr:
                curr.remove(s[curr_left])
                curr_left += 1
            curr.add(s[i])
            output = max(len(curr),output)
        return output