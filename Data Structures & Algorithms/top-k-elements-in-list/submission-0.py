from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = Counter(nums)
        sorted_d = list(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)).keys())
        for i in range(k):
            res.append(sorted_d[i])
        return res