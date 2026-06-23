from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, frequency in counts.items():
            bucket[frequency].append(num)
            
        
        res = []
        
        # Scan buckets backwards from highest frequency
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                
                # Stop immediately once we find k elements
                if len(res) == k:
                    return res
