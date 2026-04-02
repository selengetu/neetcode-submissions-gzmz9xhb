class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charS = set()
        maxS = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l +=1
            charS.add(s[r])
            maxS = max(maxS, r-l+1)
        return maxS
        