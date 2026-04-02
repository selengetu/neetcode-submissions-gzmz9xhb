class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
            freqMap = defaultdict(int)
            freqList = [[] for i in range(len(nums)+1)]
    

            for n in nums:
                freqMap[n] +=1
            
            for i, num in freqMap.items():
                freqList[num].append(i)
            
            res = []
            for val in range(len(freqList)-1, 0, -1):
                for v in freqList[val]:
                    res.append(v)
                    if len(res) == k:
                        return res
