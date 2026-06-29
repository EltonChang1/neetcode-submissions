class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            if i == 0:
                output.append(1)
            else:
                output.append(output[i-1] * nums[i-1])
        
        postfix = 1

        for j in range(len(nums)):
            output[len(nums)-j-1] = output[len(nums)-j-1] * postfix
            postfix = nums[len(nums)-j-1] * postfix
            
        return output
                


        