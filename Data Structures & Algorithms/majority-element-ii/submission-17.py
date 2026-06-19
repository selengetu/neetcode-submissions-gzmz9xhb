class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = {}
        res = []

        for i in range(len(nums)):
            count[nums[i]]  = 1+ count.get(nums[i], 0)

        for key in count:
            if count[key] > len(nums)//3:
                res.append(key)
        return res
                