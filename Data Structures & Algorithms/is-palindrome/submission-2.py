class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for i in s:
            if i.isalnum():
                cleaned_s += i.lower()
        return cleaned_s == cleaned_s[::-1]