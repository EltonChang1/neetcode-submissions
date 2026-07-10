class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr_array = []
        longest = 0
        for i in s:
            if i in curr_array:
                last_i = curr_array.index(i)
                l = last_i
                del curr_array[:l+1]
                curr_array.append(i)
            else:
                curr_array.append(i)
                if len(curr_array) > longest:
                    longest += 1

        return longest
