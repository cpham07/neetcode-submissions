class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in d:
                d[num] = i
            else:
                return [d[diff], i]


        