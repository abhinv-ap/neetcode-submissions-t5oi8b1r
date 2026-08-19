class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            key=''.join(sorted(i))
            if key in dic:
                dic[key].append(i)
            else:
                dic[key]=[i] 
        output=[]
        for i in dic.values():
            output.append(i)
        
        return output


