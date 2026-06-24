class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hashmap:
                return [hashmap[remainder], i]
            else:
                hashmap[nums[i]] = i
