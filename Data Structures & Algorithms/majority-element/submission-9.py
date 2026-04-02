class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        countDict = defaultdict(int)
        maxcount = 0
        maxval = ""

        for n in nums:
            countDict[n]+=1
            if countDict[n]>maxcount:
                maxcount = countDict[n]
                maxval = n
        return maxval
