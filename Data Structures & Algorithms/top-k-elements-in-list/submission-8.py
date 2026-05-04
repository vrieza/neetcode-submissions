class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]

        for val, freq in count.items():
            bucket[freq].append(val)
        
        res = []
        for i in range(len(bucket) -1 , 0, -1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res