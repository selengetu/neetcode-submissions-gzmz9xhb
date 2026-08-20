class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = {}
        res = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for c in count:
            if count[c] > len(nums)//3:
                res.append(c)
        return res