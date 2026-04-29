class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = list(count.items())
        arr.sort(key = lambda x:x[1])

        result = []
        for _ in range(k):
            result.append(arr.pop()[0])

        return result