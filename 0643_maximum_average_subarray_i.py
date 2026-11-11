
# LeetCode 643 - Maximum Average Subarray I
# Difficulty: Easy
# Approach: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        maximum_average = window_sum / k

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            current_average = window_sum / k

            if current_average > maximum_average:
                maximum_average = current_average

        return maximum_average
