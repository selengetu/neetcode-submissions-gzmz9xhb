class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramCheck = defaultdict(list)

        for s in strs:
            anagramCheck[tuple(sorted(s))].append(s)

        return list(anagramCheck.values())       