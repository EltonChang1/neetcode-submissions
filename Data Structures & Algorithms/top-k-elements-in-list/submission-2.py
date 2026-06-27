class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) +1
        
        sorted_hashmap = sorted(
            hashmap.keys(),
            key = lambda num : hashmap[num],
            reverse = True)

        for j in range(k):
            output.append(sorted_hashmap[j])
        return output
        