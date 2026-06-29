class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            check = target - numbers[i]
            if check in hashmap:
                return [hashmap[check]+1,i+1]
            hashmap[numbers[i]] = i
