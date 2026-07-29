class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set()

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashset:
                comp_ind = nums.index(comp)
                return [comp_ind,i]
            else:
                hashset.add(nums[i])