class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        for i in range(len(nums)):
            hashset = set()

            for j in range(i+1,len(nums),1):
                check = -nums[i] - nums[j]
                if check in hashset:
                    triplet = tuple(sorted([nums[i],nums[j],check]))
                    output.add(triplet)
                hashset.add(nums[j])

        return [list(triplet) for triplet in output]

        


        