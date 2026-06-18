class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [ [] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for ind, num in count.items():
            freq[num].append(ind)

        ans = []

        for i in range(len(freq)-1, 0, -1):
            for s in freq[i]:
                ans.append(s)

                if len(ans) == k:
                    return ans

 