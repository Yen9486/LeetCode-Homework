class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        avgs = [-1] * n
        
        window_size = 2 * k + 1
        
        if n < window_size:
            return avgs
        
        current_window_sum = sum(nums[:window_size])
        
        avgs[k] = current_window_sum // window_size
        
        for i in range(window_size, n):
            current_window_sum += nums[i] - nums[i - window_size]
            
            avgs[i - k] = current_window_sum // window_size
            
        return avgs