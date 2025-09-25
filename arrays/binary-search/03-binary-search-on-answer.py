import math
from typing import List


class Solution:
    def squareRoot(self, n: int):
        """
        Find square root of a number
        Link: https://leetcode.com/problems/sqrtx/description/

        Given a non-negative integer x, return the square root of x rounded down
        to the nearest integer. The returned integer should be non-negative as well.
        """

        if n <= 1:
            return n

        # We add "1" because in this particular binary search
        # template, right is not inclusive in the answer.
        left, right = 0, (n // 2) + 1
        while left < right:
            # To avoid overflow - although python doesn't
            # really have them but even in python, big integer
            # arithmetic is slower than usual so why not.
            mid = left + (right - left) // 2
            if mid * mid > n:
                right = mid
            else:
                left = mid + 1
        return left - 1

    def nthRoot(self, n: int, m: int):
        """
        Finding nth root of m
        Link: https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

        You are given 2 numbers n and m, the task is to find n√m (nth root of m).
        If the root is not integer then returns -1.
        """

        if n == 1:
            return m
        if m <= n:
            return -1

        # Since we have handled the edge cases above,
        # the search space with `m // n` makes sense here.
        left, right = 0, m // n
        while left < right:
            mid = left + (right - left) // 2

            if mid**n >= m:
                right = mid
            else:
                left = mid + 1

        return left if (left**n) == m else -1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko eating bananas
        Link: https://leetcode.com/problems/koko-eating-bananas/description/

        Koko has n piles of bananas, with piles[i] bananas in the i-th pile.
        She can eat at a fixed speed of k bananas per hour. Each hour, she eats from
        one pile:
        - If the pile has ≥ k bananas, she eats k.
        - If the pile has < k bananas, she finishes that pile and stops for that hour.

        Koko wants the smallest possible k that still allows her to finish all bananas
        within h hours. Find the minimum integer eating speed k so that Koko finishes
        all bananas within h hours.
        """

        def isPossibleSpeed(max_speed: int):
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / max_speed)
                # Early termination
                if hours > h:
                    return False
            return True

        # The "right" part is tricky. max(piles) will work just fine.
        # This is more of an optimization that comes with practice.
        # The reasoning is like this:
        #
        # If `h` is huge, the answer will lie more on the lower spectrum. So,
        # we allow koko to eat 1 banana per hour and then divide the rest of
        # the bananas with the leftover `h`.
        #
        # low, high = math.ceil(sum(piles) / h), min(
        #     max(piles), math.ceil((sum(piles) - len(piles) + 1) / (h - len(piles) + 1))
        # )
        left, right = math.ceil(sum(piles) / h), max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if isPossibleSpeed(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Capacity To Ship Packages Within D Days
        Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

        A conveyor belt has packages that must be shipped from one port to another within
        days days.

        The ith package on the conveyor belt has a weight of weights[i]. Each day, we load
        the ship with packages on the conveyor belt (in the order given by weights). We may
        not load more weight than the maximum weight capacity of the ship.

        Return the least weight capacity of the ship that will result in all the packages on
        the conveyor belt being shipped within days days.
        """

        def isPossibleCapacity(capacity):
            # NOTE: This is important, starting with "1". You
            # miss this quite often.
            num_days, current_weight = 1, 0
            for weight in weights:
                current_weight += weight
                if current_weight + weight <= capacity:
                    current_weight += weight
                else:
                    num_days += 1
                    current_weight = weight
                    # Early termination, a quick optimization
                    if num_days > days:
                        return False
            return True

        left, right = max(weights), sum(weights) + 1
        while left < right:
            mid = left + (right - left) // 2

            if isPossibleCapacity(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        Maximum Candies Allocated to K Children
        Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/

        You are given a 0-indexed integer array candies. Each element in the array
        denotes a pile of candies of size candies[i]. You can divide each pile into
        any number of sub piles, but you cannot merge two piles together.

        You are also given an integer k. You should allocate piles of candies to k
        children such that each child gets the same number of candies. Each child
        can be allocated candies from only one pile of candies and some piles of
        candies may go unused.

        Return the maximum number of candies each child can get.
        """

        def isPossibleSplit(max_candies):
            count = 0
            for num_candy in candies:
                count += num_candy // max_candies
            return count >= k

        if sum(candies) < k:
            return 0

        left, right = 1, min(max(candies) + 1, math.ceil(sum(candies) / k) + 1)
        while left < right:
            mid = left + (right - left) // 2

            # Note: Here, we flipped the conditions. This is actually
            # very intuitive. We want to find the maximum possible answer,
            # so we will move mid to the right in case our feasibility
            # condition is true.
            if isPossibleSplit(mid):
                left = mid + 1
            else:
                right = mid

        # We return left - 1 because we are reversing the condition
        return left - 1

    def aggressiveCows(self, stalls, k):
        """
        Aggressive Cows
        Link: https://www.geeksforgeeks.org/problems/aggressive-cows/1

        You are given an array with unique elements of stalls[], which denote the
        positions of stalls. You are also given an integer k which denotes the number
        of aggressive cows. The task is to assign stalls to k cows such that the
        minimum distance between any two of them is the maximum possible.
        """

        def isPossibleDistance(distance):
            last = stalls[0]
            count = 1
            for i in range(1, len(stalls)):
                if stalls[i] - last >= distance:
                    count += 1
                    last = stalls[i]
                if count == k:
                    return True
            return False

        stalls.sort()
        left, right = 1, stalls[-1] - stalls[0] + 1
        while left < right:
            mid = left + (right - left) // 2
            # To maximize a minimum, again we have flipped the conditions
            if isPossibleDistance(mid):
                left = mid + 1
            else:
                right = mid

        # We return left - 1 because we are reversing the condition
        return left - 1

    def findPages(self, arr, k):
        """
        Allocate Minimum Pages
        Link: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

        Given an array arr[] of integers, where each element arr[i] represents
        the number of pages in the i-th book. You also have an integer k
        representing the number of students. The task is to allocate books to
        each student such that:

        - Each student receives atleast one book.
        - Each student is assigned a contiguous sequence of books.
        - No book is assigned to more than one student.

        The objective is to minimize the maximum number of pages assigned to any
        student. In other words, out of all possible allocations, find the arrangement
        where the student who receives the most pages still has the smallest possible maximum.

        Note: If it is not possible to allocate books to all students, return -1.
        """

        if len(arr) < k:
            return -1

        def isPossibleAllocation(pages):
            count = 1
            current_pages = 0
            for num_pages in arr:
                if current_pages + num_pages <= pages:
                    current_pages += num_pages
                else:
                    count += 1
                    current_pages = num_pages

                    if count > k:
                        return False
            return True

        left, right = max(arr), sum(arr) + 1
        while left < right:
            mid = left + (right - left) // 2

            if isPossibleAllocation(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Magnetic Force Between Two Balls
        Link: https://leetcode.com/problems/magnetic-force-between-two-balls/description/

        In the universe Earth C-137, Rick discovered a special form of magnetic force
        between two balls if they are put in his new invented basket. Rick has n empty
        baskets, the ith basket is at position[i], Morty has m balls and needs to
        distribute the balls into the baskets such that the minimum magnetic force
        between any two balls is maximum.

        Rick stated that magnetic force between two different balls at positions
        x and y is |x - y|.

        Given the integer array position and the integer m. Return the required force.
        """

        def isPossibleForce(max_force):
            previous = position[0]
            count = 1
            for i in range(1, len(position)):
                if position[i] - previous >= max_force:
                    count += 1
                    previous = position[i]
                    # Note: This is the early termination condition
                    # We need to make sure that we are able to place
                    # at least "m" balls, if we can place more, then
                    # also it's fine but it can't be less.
                    if count >= m:
                        return True
            return False

        position.sort()
        left, right = 1, position[-1] - position[0] + 1
        while left < right:
            mid = (left + right) >> 1
            # Since we are finding "Maximum of minimum",
            # the conditions have been reversed
            if isPossibleForce(mid):
                left = mid + 1
            else:
                right = mid
        # # We return left - 1 because we are reversing the condition
        return left - 1

    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Split Array Largest Sum
        Link: https://leetcode.com/problems/split-array-largest-sum/description/

        Given an integer array nums and an integer k, split nums into k
        non-empty subarrays such that the largest sum of any subarray is minimized.

        Return the minimized largest sum of the split.
        """

        def isPossibleSplit(max_sum):
            splits = 1
            current_sum = 0
            for num in nums:
                if current_sum + num <= max_sum:
                    current_sum += num
                else:
                    splits += 1
                    current_sum = num

                    if splits > k:
                        return False
            return True

        left, right = max(nums), sum(nums) + 1
        while left < right:
            mid = left + (right - left) // 2

            if isPossibleSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left

    # A little different Binary Search Problem and respective template
    #
    # The answer can be any value between 0.0 and stations[n-1] - stations[0], since that's
    # the maximum possible distance between any two stations.
    # We use binary search in this range. For each value d, we check:
    # - If we can insert k or fewer gas stations such that the maximum distance between any
    #   two stations is at most d, then this d could be a possible answer. So, we try to
    #   reduce the range and look for a smaller d.
    # - If we need to insert more than k stations, then d is too small, so we increase d.
    #
    # Points to remember:
    # - Since the answer needs to be accurate to 2 decimal places, we can't use the condition
    # low >= high in binary search. This is because decimal values can lead to infinite loops
    # due to precision issues.
    #
    # - Also, we can't do low = mid + 1 or high = mid - 1 like we do in integer binary search.
    # Since the answer is a double, jumping by 1 would skip over valid decimal values.
    def minMaxDist(self, stations, k):
        """
        Minimize Max Distance to Gas Station
        Link: https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

        We have a horizontal number line. On that number line, we have gas stations
        at positions stations[0], stations[1], ..., stations[n-1]. Now, we add k
        more gas stations so that d, the maximum distance between adjacent gas stations,
        is minimized. We have to find the smallest possible value of d. Find the answer
        exactly to 2 decimal places.

        Note: stations is in a strictly increasing order.
        """

        def isPossibleDistance(distance):
            station_count = 0
            for i in range(1, len(stations)):
                # Use pen and paper with some examples, this
                # will become quite clear.
                gap = stations[i] - stations[i - 1]
                station_count += (math.ceil(gap) / distance) - 1
                if station_count > k:
                    return False
            return station_count <= k

        left, right = 0, stations[-1] - stations[0] + 1
        # NOTE: Since the precision required in the answer is 2,
        # we use 1e-3. (In general, 1e-(N + 1) where N is the req precision)
        while right - left > 1e-3:
            mid = left + (right - left) / 2

            # In this type of inary search problem, we do not
            # increment the boundaries by 1. That will lead
            # us to miss hell lot of possibilities from the search space.
            if isPossibleDistance(mid):
                right = mid
            else:
                left = mid

        return left
