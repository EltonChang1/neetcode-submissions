class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for ind, num in enumerate(nums):
            check = target - num
            if check in hashmap:
                return [hashmap[check],ind]
            hashmap[num] = ind


