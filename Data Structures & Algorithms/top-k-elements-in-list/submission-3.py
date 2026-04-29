class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize list from length of nums, represent min to max frequency
        buckets = [[] for _ in range (len(nums)+1)]
        count=Counter(nums)
        result = []
        print(
            "initialized buckets ->",
            buckets
        )

        # iterate Counter
        for ele, freq in count.items():
            # Put elements that have same frequency.
            buckets[freq].append(ele)
            print ("added -> ", buckets)

        # Go backwards from highest frequency bucket
        print("loop target -> ", range(len(buckets) - 1, 0, -1))
        for i in range(len(buckets) - 1, 0, -1):
            print("i ->", i, "buckets :", buckets[i])
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result