class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freq = []
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1

        for num, freqs in d.items():
            buckets[freqs].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                freq.append(num)
                if len(freq) == k:
                    return freq



        

        return freq

        