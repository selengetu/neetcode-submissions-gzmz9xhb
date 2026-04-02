from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same length
        if len(s) != len(t):
            return False
        
        # Count the frequency of each character in both strings
        return Counter(s) == Counter(t)

# Example 1
s1 = "racecar"
t1 = "carrace"
solution = Solution()
print(solution.isAnagram(s1, t1))  # Output: True

# Example 2
s2 = "jar"
t2 = "jam"
print(solution.isAnagram(s2, t2))  # Output: False

        