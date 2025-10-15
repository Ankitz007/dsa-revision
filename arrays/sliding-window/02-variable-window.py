from collections import Counter, defaultdict
from typing import List


# Function to find the length of the longest substring with exactly K unique characters
def longestKSubstr(nums, k):
    """
    Longest Substring with K Uniques
    Problem: Find the length of the longest substring with exactly K unique characters.
    If no such substring exists, return -1.
    Time: O(N)
    Space: O(1) [Map can have at most 26 lowerdigit characters]
    """
    left = right = longest = 0
    uniques, window_map = 0, defaultdict(int)

    while right < len(nums):
        window_map[nums[right]] += 1
        if window_map[nums[right]] == 1:  # New unique character added to window
            uniques += 1

        # Shrink window until we have at most k unique characters
        while uniques > k:
            window_map[nums[left]] -= 1
            if window_map[nums[left]] == 0:  # Unique character removed from window
                uniques -= 1
            left += 1

        # Update longest if window has exactly k unique characters
        if uniques == k:
            longest = max(longest, right - left + 1)
        right += 1

    return longest if longest else -1


# Function to find the length of the longest substring without repeating characters
def lengthOfLongestSubstring(s: str) -> int:
    """
    Longest Substring Without Repeating Characters
    Problem: Find the length of the longest substring without repeating characters.
    Time: O(N)
    Space: O(1) [Map can have at most characters, symbols and spaces]
    """
    left = right = longest = 0
    seen = defaultdict(lambda: -1)  # Stores last seen index of each character

    while right < len(s):
        char = s[right]
        # If character is repeated in current window, move left pointer
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        seen[char] = right  # Update last seen index

        longest = max(longest, right - left + 1)  # Update answer
        right += 1

    return longest


# Function to find the maximum number of consecutive 1's with at most k flips of 0's
def longestOnes(nums: List[int], k: int) -> int:
    """
    Max Consecutive Ones III
    Problem: Given a binary array nums and an integer k, return the maximum number
    of consecutive 1's in the array if you can flip at most k 0's.
    Time: O(N)
    Space: O(1)
    """
    left = right = zeros = answer = 0

    while right < len(nums):
        if nums[right] == 0:
            zeros += 1  # Count zeros in current window

        # If zeros exceed k, shrink window from left
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Update answer if window is valid
        if zeros <= k:
            answer = max(answer, right - left + 1)
        right += 1

    return answer


# Function to count substrings containing at least one 'a', 'b', and 'c'
def numberOfSubstrings(s: str) -> int:
    """
    Number of Substrings Containing All Three Characters
    Problem: Given a string s, return the number of substrings that contain at
    least one occurrence of all three characters: 'a', 'b', and 'c'.
    """
    length = len(s)
    left = right = length - 1
    answer = 0
    window_map = defaultdict(int)
    window_count = 0  # Number of unique characters in window

    while left >= 0:
        window_map[s[left]] += 1
        if window_map[s[left]] == 1:
            window_count += 1  # New unique character added

        # If window contains all three characters, count substrings
        while window_count == 3:
            answer += left + 1  # All substrings starting at left and ending at right
            window_map[s[right]] -= 1
            if window_map[s[right]] == 0:
                window_count -= 1  # Unique character removed
            right -= 1

        left -= 1

    return answer


# Function to find the length of the longest substring after at most k replacements
def characterReplacement(s: str, k: int) -> int:
    """
    Longest Repeating Character Replacement
    Problem: You are given a string s and an integer k. You can choose any character
    of the string and change it to any other uppercase English character.
    You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get
    after performing the above operations.
    Time: O(N)
    Space: O(1)
    """
    left = right = longest = max_freq = 0
    window_map = defaultdict(int)

    while right < len(s):
        window_map[s[right]] += 1
        max_freq = max(
            max_freq, window_map[s[right]]
        )  # Track most frequent character in window

        # If more than k replacements needed, shrink window
        if right - left + 1 - max_freq > k:
            window_map[s[left]] -= 1
            left += 1

        longest = max(longest, right - left + 1)  # Update answer
        right += 1

    return longest


# Function to count number of subarrays with sum equal to goal
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    """
    Binary Subarrays With Sum
    Problem: Given a binary array nums and an integer goal, return the number of
    non-empty subarrays with a sum equal to goal.
    Time: O(N) [actually O(4N)]
    Space: O(1)
    Note: Can be done in strictly O(N) using PrefixSum.
    """

    def sliding_window(goal):
        if goal < 0:
            return 0
        left = right = window_sum = count = 0

        while right < len(nums):
            window_sum += nums[right]

            # Shrink window if sum exceeds goal
            while window_sum > goal:
                window_sum -= nums[left]
                left += 1

            count += right - left + 1  # Count valid subarrays ending at right
            right += 1

        return count

    # Number of subarrays with sum == goal is difference of two sliding windows
    return sliding_window(goal) - sliding_window(goal - 1)


# Function to find the minimum window substring containing all characters of t
def minWindow(s: str, t: str) -> str:
    """
    Minimum Window Substring
    Problem: Given two strings s and t of lengths m and n respectively,
    return the minimum window substring of s such that every character in
    t (including duplicates) is included in the window. If there is no
    such substring, return the empty string "".
    Time: O(m + n)
    Space: O(m + n)
    """
    if not s or not t or len(s) < len(t):
        return ""

    need, min_len = Counter(t), float("inf")  # Characters needed and min window length
    required = len(need)  # Number of unique characters needed
    left = right = formed = min_left = 0
    window_counts = {}

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If current character fulfills the need, increment formed
        if char in need and window_counts[char] == need[char]:
            formed += 1

        # Try to shrink window from left while all needs are fulfilled
        while formed == required:
            char = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            window_counts[char] -= 1
            if char in need and window_counts[char] < need[char]:
                formed -= 1
            left += 1

        right += 1

    # Return minimum window substring or empty string if not found
    return "" if min_len == float("inf") else s[min_left : min_left + min_len]
