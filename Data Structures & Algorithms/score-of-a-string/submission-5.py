class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for c in range(1, len(s)):
            score += abs(ord(s[c])- ord(s[c-1]))
        return score
