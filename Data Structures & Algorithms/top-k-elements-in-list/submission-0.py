class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            count = counts.get(num,0)
            counts[num] = count+1

        return sorted(counts.keys(),reverse=True,key=lambda x: counts[x])[:k]
        