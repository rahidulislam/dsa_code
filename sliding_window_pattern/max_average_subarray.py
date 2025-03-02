from typing import List


class Solution:
    def findMaxAverage(self,nums:List[int], k:int)->float:
        if k > len(nums):
            return None
        max_average = 0
        window_sum = sum(nums[:k])
        max_average = window_sum / k
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k ] + nums[i]
            max_average = max(max_average, window_sum / k)
        return max_average

s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75   
# Time complexity: O(n)
# Space complexity: O(1)
