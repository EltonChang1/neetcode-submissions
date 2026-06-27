class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) +1
        
        for j in range(k):
            max_key = max(hashmap, key=hashmap.get)
            output.append(max_key)
            del hashmap[max_key]
        
        return output
        