class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maxCount = 0
        maxNum = nums[0]
        dic = {}

        for i in range(len(nums)):
            dic[nums[i]] = 1 + dic.get(nums[i], 0)

            if dic[nums[i]] > maxCount:
                maxCount = dic[nums[i]]
                maxNum = nums[i]
        return maxNum

