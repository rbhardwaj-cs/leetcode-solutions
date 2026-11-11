# LeetCode 643 - Maximum Average Subarray I
# Difficulty: Easy
# Approach: Brute Force (Window Enumeration)
# Time Complexity: O(n * k)
# Extra Space Complexity: O(k)

class Solution(object):
    def findMaxAverage(self, nums, k):
        maximum_average = float(sum(nums[0:k]) / k)
        for i in range(0, len(nums) - k + 1):
            if maximum_average < sum(nums[i:i+k]) / k:
                maximum_average = sum(nums[i:i+k]) / k
        return maximum_average
