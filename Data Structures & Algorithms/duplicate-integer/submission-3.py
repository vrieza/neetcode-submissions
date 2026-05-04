class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count  = Counter(nums)
        for val,freq in count.items():
            if count.get(val) > 1:
                return True
        return False