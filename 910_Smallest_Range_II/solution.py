class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        res = nums[-1] - nums[0]
        
        for i in range(n - 1):
            high = max(nums[i] + k, nums[n - 1] - k)
            
            low = min(nums[0] + k, nums[i + 1] - k)
            
            res = min(res, high - low)
            
        return res