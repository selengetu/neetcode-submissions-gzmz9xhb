class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res = []

        for o in operations:
            if res and o == '+':
                res.append(res[-1] + res[-2])
            elif res and o == 'D':
                res.append(res[-1] *2)
            elif res and o == 'C':
                res.remove(res[-1])
            else:
                res.append(int(o))
        return sum(res)
