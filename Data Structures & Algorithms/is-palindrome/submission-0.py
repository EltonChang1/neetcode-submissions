class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        cleaned = ""
        for i in s:
            if i.isalnum():         #.isalnum() checks whether a 
                                    #character/string is alphanumeric.
                cleaned += i

        list_s = list(cleaned)
        front = 0
        end = len(cleaned)-1
        while front < end:
            if list_s[front] != list_s[end]:
                return False
            else:
                front += 1
                end -= 1
        return True
        