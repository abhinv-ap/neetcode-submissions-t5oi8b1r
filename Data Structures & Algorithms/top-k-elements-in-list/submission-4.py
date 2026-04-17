from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        for i in nums:
            a[i] += 1
        sorted_items = sorted(a.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(sorted_items[i][0])
            
        return ans
        