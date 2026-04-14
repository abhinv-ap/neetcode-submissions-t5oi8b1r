from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        a = defaultdict(int)
        for i in nums:
            a[i] += 1

        # 2. Sort by values (descending) 
        # Fix: The closing parenthesis for sorted() was in the wrong place
        sorted_items = sorted(a.items(), key=lambda item: item[1], reverse=True)
        
        # 3. Extract the top K keys
        # Fix: We only need the keys, not the full items (key, value)
        ans = []
        for i in range(k):
            ans.append(sorted_items[i][0])
            
        return ans
        