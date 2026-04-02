class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        allcnt = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            freq[n] +=1
        
        for num, count in freq.items():
            allcnt[count].append(num)

        
        for i in range(len(allcnt)-1, 0, -1):
            for na in allcnt[i]:
                res.append(na)
                if len(res) == k:
                    return res
            