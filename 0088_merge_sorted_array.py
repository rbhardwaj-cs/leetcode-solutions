# LeetCode 88 - Merge Sorted Array
# Difficulty: Easy
# Approach: Three Pointers (Right to Left)
# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        write = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1

            write -= 1

        while p2 >= 0:
            nums1[write] = nums2[p2]
            p2 -= 1
            write -= 1
