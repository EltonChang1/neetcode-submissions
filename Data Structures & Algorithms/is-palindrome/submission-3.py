class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        
        for i in s:
            if i.isalnum():
                cleaned = cleaned + i.lower()
        
        return cleaned == cleaned[::-1]
