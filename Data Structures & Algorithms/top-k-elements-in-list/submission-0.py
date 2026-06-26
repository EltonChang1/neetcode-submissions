class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                hashmap[nums[i]] += 1

        output = list()
        for i in range(k):
            cur_max=max(hashmap, key = hashmap.get)
            output.append(cur_max)
            hashmap.pop(cur_max, None)
        
        return output


        