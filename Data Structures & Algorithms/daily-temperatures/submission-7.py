class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        tmp = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                tmp[stackInd] = i - stackInd

            stack.append((t, i))
        return tmp