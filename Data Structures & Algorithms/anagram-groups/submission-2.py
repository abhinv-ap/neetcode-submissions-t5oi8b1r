class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ktov={}
        res=[]
        for i in strs:
            key=''.join(sorted(i))
            if key not in ktov:
                ktov[key] = []
            ktov[key].append(i)
        
        for i in ktov.values():
            res.append(i)
        
        return res

        
        