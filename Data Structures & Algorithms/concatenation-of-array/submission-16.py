class Solution:
    def getConcatenation(self, nums: list[int])-> list[int]:

        l = len(nums)
        ans = [0] * 2 * l

        for i, n in enumerate(nums):
            ans[i] = ans[i+l] = n
        return ans
