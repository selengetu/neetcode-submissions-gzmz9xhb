class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""
        for c in strs:
            s += str(len(c)) + "#" + c
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move i to beginning of actual string
            i = j + 1

            # j becomes end of actual string
            j = i + length

            # Extract string
            res.append(s[i:j])

            # Move to next encoded string
            i = j

        return res

        
        
