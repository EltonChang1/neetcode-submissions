class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        if len(nums) == 0:
            return 0

        longest = 1
        cur_longest = 1
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]-1:
                cur_longest += 1
                if cur_longest > longest:
                    longest = cur_longest
            elif sorted_nums[i] == sorted_nums[i+1]:
                continue
            else :
                cur_longest = 1
            
        return longest

        