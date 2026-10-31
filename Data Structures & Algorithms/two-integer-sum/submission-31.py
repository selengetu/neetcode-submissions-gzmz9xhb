class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i, num in enumerate(nums):

            diff = target - nums[i]

            if diff in dic:
                return [dic[diff], i ]
            
            dic[num] = i