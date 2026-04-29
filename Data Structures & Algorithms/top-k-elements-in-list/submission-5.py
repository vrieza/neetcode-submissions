class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize list from length of nums, represent min to max frequency
        count = Counter(nums)
        arr = list(count.items())
        arr.sort(key = lambda x:x[1])
        print(arr)
        result = []
        for _ in range(k):
            result.append(arr.pop()[0])
            print(result)
        return result