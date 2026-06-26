class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            temp_list = nums.copy()
            temp_list.pop(i)
            product = 1
            for j in temp_list:
                product = product * j
            output.append(product)
        return output