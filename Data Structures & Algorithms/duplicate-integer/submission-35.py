class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        uniq_num = set()

        for i in range(len(nums)):
            if nums[i] in uniq_num:
                return True
            else:
                uniq_num.add(nums[i])
        return False