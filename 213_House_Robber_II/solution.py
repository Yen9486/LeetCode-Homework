class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        def helper(start, end):
            rob1, rob2 = 0, 0
            for i in range(start, end):
                temp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
            
        n = len(nums)
        
        rob_first = helper(0, n - 1)
        
        rob_last = helper(1, n)
        
        return max(rob_first, rob_last)