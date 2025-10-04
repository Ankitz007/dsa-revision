from typing import List


class Solution:
    def lowerBound(self, arr, target):
        """
        Implement Lower Bound
        Link: https://www.geeksforgeeks.org/problems/implement-lower-bound/1

        The lower bound of a number is defined as the smallest index in the
        sorted array where the element is greater than or equal to the given
        number.
        """
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            # Basically, if the element is greater than or
            # equal to target, it CAN be the answer.
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def upperBound(self, arr, target):
        """
        Implement Upper Bound
        Link: https://www.geeksforgeeks.org/problems/implement-upper-bound/1

        The upper bound of a number is defined as the smallest index in the
        sorted array where the element is greater than the given number.
        """
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            # Basically, if the element is greater than
            # target, it CAN be the answer.
            if arr[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

    def findPeakElement(self, nums: List[int]) -> int:
        """
        Find Peak Element
        Link: https://leetcode.com/problems/find-peak-element/description/

        A peak element is an element that is strictly greater than its neighbors.

        Given a 0-indexed integer array nums, find a peak element, and return
        its index. If the array contains multiple peaks, return the index to
        any of the peaks.

        You may imagine that nums[-1] = nums[n] = -∞. In other words, an element
        is always considered to be strictly greater than a neighbor that is
        outside the array.
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            # This is slope based intuition. If element
            # at `mid` is greater than that at `mid + 1`, we know
            # it's a decreasing slope, so we know there
            # will certainly be a peak in the left half.
            #
            # It can also be equated to:
            # Finding the first index where element at `mid` position
            # is greater than element at `mid + 1`.
            #
            # The `mid == len(nums) - 1` check is so that nums[mid + 1]
            # is always safe to access.
            # You can also add a -inf to the end of the list and skip this
            # check entirely!
            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

    def searchInRotatedSortedArray(self, nums: List[int], target: int) -> int:
        """
        Search in Rotated Sorted Array
        Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

        Given the array nums after the possible rotation and an integer
        target, return the index of target if it is in nums, or -1 if it is
        not in nums.
        """
        # `right` in this particular template is inclusive, hence
        # we do `len(nums) - 1`
        left, right = 0, len(nums) - 1
        answer = -1

        # For searches, use this particular template with
        # the loop condition as this and search space
        # reduction using `mid + 1` or `mid - 1`.
        #
        # In this particular problem, we can not eliminate like
        # we were doing till now. The information is not adequate
        # for elimination of a certain half.
        #
        # The intuition: At least one half is always sorted in a
        # sorted array which has been rotated.
        # So, we compare element at `mid` with `left` and `right`
        # elements. This tells us which half is sorted. Rest is
        # simple binary search.
        while left <= right:
            mid = left + (right - left) // 2
            # Gotcha!
            if nums[mid] == target:
                answer = mid
                break
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return answer

    def findMinInRotatedSortedArray(self, nums: List[int]) -> int:
        """
        Find Minimum in Rotated Sorted Array
        Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

        Given the sorted rotated array nums of unique elements,
        return the minimum element of this array.
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # Basically, if the right half is sorted, the minimum
            # will not be in this half.
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        Peak Index in a Mountain Array
        Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

        You are given an integer mountain array arr of length n where the
        values increase to a peak element and then decrease. Return the
        index of the peak element.
        """
        # The constraints allow us to use `len(arr) -1` because
        # the list will always have at least 3 elements.
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            # Basically, find the first index where the slope
            # begins descending.
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Single Element in a Sorted Array
        Link: https://leetcode.com/problems/single-element-in-a-sorted-array/description/

        You are given a sorted array consisting of only integers where every
        element appears exactly twice, except for one element which appears
        exactly once.

        Return the single element that appears only once.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if mid % 2 == 1:
                mid -= 1

            # Note: This is the logic we employ to judge which half
            # will contain the single element. If a number is
            # present in pairs, the even and the corresponding odd
            # index should be same. If they aren't, the single element
            # lies in the right half.
            # Since se already checked for mid + 1, we update left to
            # `mid + 2`.
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
