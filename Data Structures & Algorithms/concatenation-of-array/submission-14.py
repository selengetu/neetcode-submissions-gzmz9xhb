class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       
        l = len(nums)
        ans = [0] * l * 2

        for i, n in enumerate(nums):
            ans[i] = ans[i+l] = n
        return ans
