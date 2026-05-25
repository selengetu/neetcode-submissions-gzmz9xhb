class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maxcount = 0
        maxnum = 0

        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
            if count[nums[i]] > maxcount:
                maxcount = count[nums[i]]
                maxnum = nums[i]
        return maxnum
