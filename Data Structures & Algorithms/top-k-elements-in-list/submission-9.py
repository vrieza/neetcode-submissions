class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for x in range(len(nums)+1)]
        for key, freq in count.items():
            bucket[freq].append(key)

        res=[]
        for freq in range(len(bucket)-1, 0, -1):
            for val in bucket[freq]:
                res.append(val)
                if len(res) == k:
                    return res