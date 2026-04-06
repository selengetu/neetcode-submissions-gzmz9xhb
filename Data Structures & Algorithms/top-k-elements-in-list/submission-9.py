class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
            freqMap = defaultdict(int)
            freq = [[] for i in range(len(nums)+1)]
            res = []

            for n in nums:
                freqMap[n] +=1
            
            for i, num in freqMap.items():
                freq[num].append(i)
            
            for i in range(len(freq)-1, 0, -1):
                for number in freq[i]:
                    res.append(number)
                    if len(res) == k:
                        return res
                        

