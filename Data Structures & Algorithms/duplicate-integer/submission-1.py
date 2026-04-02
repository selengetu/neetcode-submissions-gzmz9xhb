from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example 1
nums1 = [1, 2, 3, 3]
solution = Solution()
print(solution.hasDuplicate(nums1))  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(solution.hasDuplicate(nums2))  # Output: False

         