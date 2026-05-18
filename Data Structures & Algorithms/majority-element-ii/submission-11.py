class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count = defaultdict(int)

        for n in nums:
            count[n]+=1
        for c in count:
            if count[c] > len(nums) // 3:
                res.append(c)
        return res