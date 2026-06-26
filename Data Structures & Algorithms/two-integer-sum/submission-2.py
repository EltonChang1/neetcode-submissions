class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            check = target - nums[i]
            if check in hashmap:
                return [hashmap.get(check),i]
            else:
                hashmap[nums[i]] = i
            