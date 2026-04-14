class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        freqset = [[] for i in range(len(nums)+1)]

        ans = []
        for n in nums:
            freq[n] +=1
        
        for i, num in freq.items():
            freqset[num].append(i)
        
        for index in range(len(freqset)-1, -1, -1):
            for n in freqset[index]:
                ans.append(n)
                if len(ans) == k:
                    return ans

