class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maxcount = 0
        maxnum = 0
        freq = {}

        for n in nums:
            freq[n] = 1+ freq.get(n, 0)
            if freq[n] > maxcount:
                maxcount = freq[n]
                maxnum = n
        return maxnum
