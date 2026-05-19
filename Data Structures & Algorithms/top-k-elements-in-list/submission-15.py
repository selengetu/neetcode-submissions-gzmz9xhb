class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqcount = {}
        ans = [[] for i in range(len(nums)+1)]
        res = []

        for i in range(len(nums)):
            freqcount[nums[i]] = 1 + freqcount.get(nums[i], 0)
        
        for i, n in freqcount.items():
            ans[n].append(i)

        for i in range(len(ans)-1, 0, -1):
            for n in ans[i]:
                res.append(n)
                if len(res) == k:
                    return res
