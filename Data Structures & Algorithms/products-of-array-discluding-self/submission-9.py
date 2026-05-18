class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        posfix = 1

        ans = [1] * (len(nums))

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= posfix
            posfix *= nums[i]
        
        return ans


        


