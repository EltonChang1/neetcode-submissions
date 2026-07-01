class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
                postfix.append(1)
            
            else:
                prefix.append(nums[i-1] * prefix[i-1])
                postfix.append(nums[len(nums)-i] * postfix[i-1])
        postfix = postfix[::-1]

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])

        return output
        
        
