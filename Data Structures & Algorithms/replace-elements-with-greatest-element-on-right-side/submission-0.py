class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)
        maxval = -1
        for i in range(n-1, -1, -1):
            curr = arr[i]
            arr[i] = maxval
            maxval= max(arr[i],curr)
        return arr
    
            