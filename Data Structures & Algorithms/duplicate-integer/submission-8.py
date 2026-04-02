from typing import List

class Solution:
      def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:  # Check if the number is already in the set
                return True
            seen.add(i)  # Add the number to the set
        return False 
