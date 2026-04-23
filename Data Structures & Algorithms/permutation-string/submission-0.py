class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = {}
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            # shrink if too many of this char
            while window[c] > need.get(c, 0):
                window[s2[l]] -= 1
                l += 1

            # check window size
            if r - l + 1 == len(s1):
                return True

        return False