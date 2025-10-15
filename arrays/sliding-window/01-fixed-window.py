from collections import Counter, defaultdict, deque
from typing import List


def maximumSumSubarray(arr, k):
    """
    Max Subarray Sum of Size K
    Problem: Given an array of integers and a number k, find the maximum sum of a subarray of size k.
    TC: O(N)
    SC: O(1)
    """
    left = right = result = current_sum = 0

    while right < len(arr):
        current_sum += arr[right]

        if right - left + 1 == k:
            result = max(result, current_sum)
            current_sum -= arr[left]
            left += 1

        right += 1

    return result


def search(pat, txt):
    """
    Count occurrences of anagrams
    Problem: Given a text and a pattern, find all occurrences of anagrams of the pattern in the text.
    TC: O(N)
    SC: O(1) because number of characters is fixed (26 for lowercase English letters)
    """
    left = right = result = 0
    pat_map = Counter(pat)
    count = len(pat_map)

    while right < len(txt):
        pat_map[txt[right]] -= 1
        if pat_map[txt[right]] == 0:
            count -= 1

        if right - left + 1 == len(pat):
            if count == 0:
                result += 1
            pat_map[txt[left]] += 1
            if pat_map[txt[left]] == 1:
                count += 1
            left += 1

        right += 1

    return result


def firstNegInt(arr, k):
    """
    First Negative Integer in Every Window of Size K
    Problem: Given an array and a number k, find the first negative integer in every window of size k.
    TC: O(N)
    SC: O(K)
    """
    queue = deque()
    left = right = 0
    result = []

    while right < len(arr):
        if arr[right] < 0:
            queue.append(right)

        if right - left + 1 == k:
            if queue:
                result.append(arr[queue[0]])
            else:
                result.append(0)
            if queue and queue[0] == left:
                queue.popleft()
            left += 1
        right += 1

    return result


def maxOfSubarrays(arr, k):
    """
    K-Sized subarrays maximum
    Problem: Given an array and a number k, find the maximum element in every subarray of size k.
    TC: O(N)
    SC: O(K)
    """
    left = right = 0
    result, queue = [], deque()

    while right < len(arr):
        while queue and arr[queue[-1]] < arr[right]:
            queue.pop()

        queue.append(right)

        if right - left + 1 == k:
            result.append(arr[queue[0]])
            if left == queue[0]:
                queue.popleft()
            left += 1

        right += 1

    return result


def maximumSubarraySum(nums: List[int], k: int) -> int:
    """
    Maximum Sum of Distinct Subarrays With Length K
    Problem: Given an array and a number k, find the maximum sum of distinct elements in every subarray of size k.
    TC: O(N)
    SC: O(K)
    """
    left = right = max_sum = window_sum = 0
    window_count = defaultdict(int)

    while right < len(nums):
        window_count[nums[right]] += 1
        window_sum += nums[right]

        if right - left + 1 == k:
            if len(window_count) == k:
                max_sum = max(max_sum, window_sum)

            window_sum -= nums[left]
            window_count[nums[left]] -= 1
            if window_count[nums[left]] == 0:
                window_count.pop(nums[left])
            left += 1

        right += 1

    return max_sum
