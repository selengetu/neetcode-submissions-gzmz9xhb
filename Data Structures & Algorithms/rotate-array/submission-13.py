class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        tmp = [0] * l

        for i in range(len(nums)):
            tmp[(i+k)%l] = nums[i]

        nums[:] = tmp
