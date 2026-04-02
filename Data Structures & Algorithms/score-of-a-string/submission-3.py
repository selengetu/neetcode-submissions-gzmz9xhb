class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        
        for c in range(1, len(s)):
            result += abs(ord(s[c]) - ord(s[c-1]))
        return result