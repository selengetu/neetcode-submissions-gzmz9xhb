class Solution:
    def getConcatenation(self, nums: list[int])-> list[int]:

        l = len(nums)

        ans =  [0] * l * 2

        for i in range(len(nums)):
            ans[i] = ans[i+l] = nums[i]

        return ans