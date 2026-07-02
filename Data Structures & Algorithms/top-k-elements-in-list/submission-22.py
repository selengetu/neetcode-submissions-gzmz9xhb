class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        res = []

        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for ind, num in count.items():
            freq[num].append(ind)
        
        for i in range(len(freq)-1, 0, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res

        
