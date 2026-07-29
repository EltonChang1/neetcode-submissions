class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        output = []

        for i in nums:
            hashmap[i] += 1
        
        for j in range(k):
            biggest = max(hashmap, key = hashmap.get)
            output.append(biggest)
            hashmap.pop(biggest)
        
        return output