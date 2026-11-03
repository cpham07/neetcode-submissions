class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(set(nums)) == 1:
            return [nums[0]]

        freq = []
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1
        
        for i in range(k):
            freq.append(max(d, key=d.get))
            d.pop(max(d, key=d.get))

        return freq

        