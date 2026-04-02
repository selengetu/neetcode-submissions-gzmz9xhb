class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict = defaultdict(list)
        for s in strs:
            anagramDict[tuple(sorted(s))].append(s)
        return list(anagramDict.values())
