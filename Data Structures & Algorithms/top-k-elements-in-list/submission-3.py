class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = [] 
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1
        
        for i in range(k):
            key_with_biggest_value = max(freq, key=freq.get)

            output.append(key_with_biggest_value)

            del freq[key_with_biggest_value]
        return output