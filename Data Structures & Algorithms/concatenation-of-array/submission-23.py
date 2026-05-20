class Solution:
    def getConcatenation(self, nums: list[int])-> list[int]:

        l = len(nums)
        ans = l * 2 * [0]

        for i, n in enumerate(nums):
            ans[i] = ans[i+l] = n

        return ans
