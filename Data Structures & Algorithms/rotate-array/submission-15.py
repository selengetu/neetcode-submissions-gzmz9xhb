class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [0] * len(nums)
        n = len(nums)

        for i in range(len(nums)):
            tmp[(i+k)%n] = nums[i]

        nums[:] = tmp

