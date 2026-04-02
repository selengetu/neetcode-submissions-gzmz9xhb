class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        l , j = 0, 0

        while l < len(s) and j < len(t):
            if t[j] == s[l]:
                j+=1
            l+=1
        return len(t) - j

            