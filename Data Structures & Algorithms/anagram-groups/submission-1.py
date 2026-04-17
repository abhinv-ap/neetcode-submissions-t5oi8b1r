class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            a=''.join(sorted(i))
            res[a].append(i)
        return(list(res.values()))

    


    