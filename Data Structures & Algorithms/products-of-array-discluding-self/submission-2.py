class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = {}
        prefix = 1
        postfix = 1
        n = len(nums)

        for i in range(n):
            # Left side: update index i with prefix product
            hashmap[i] = hashmap.get(i, 1) * prefix
            prefix *= nums[i]

            # Right side: update index j with postfix product
            j = n - 1 - i
            hashmap[j] = hashmap.get(j, 1) * postfix
            postfix *= nums[j]

        return [hashmap[i] for i in range(n)]