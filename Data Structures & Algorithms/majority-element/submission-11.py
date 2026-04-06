class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maxCount = 0
        num = 0
        count = defaultdict(int)

        for n in nums:
            count[n] +=1

            if count[n]>maxCount:
                maxCount = count[n]
                num = n
        return num

