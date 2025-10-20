from typing import List


class StockSpanner:
    """
    Online Stock Span
    Link: https://leetcode.com/problems/online-stock-span/description/

    Design an algorithm that collects daily price quotes for some
    stock and returns the span of that stock's price for the current
    day.

    The span of the stock's price in one day is the maximum number
    of consecutive days (starting from that day and going backward)
    for which the stock price was less than or equal to the price of
    that day.

    Implement the StockSpanner class:

    - StockSpanner() Initializes the object of the class.
    - int next(int price) Returns the span of the stock's price given
    that today's price is price.
    """

    def __init__(self):
        self._stack = []
        self._count = 0

    # Basically, we have to find the index of left greater element.
    # Since this is kind of like a "stream of input" rather than a
    # given input, we can use only this method and not the other one.
    def next(self, price: int) -> int:
        # Note: We pop until we have a larger element at stack's top.
        while self._stack and price >= self._stack[-1][0]:
            self._stack.pop()

        span = 1
        if self._stack:
            span = self._count - self._stack[-1][1]
        else:
            span = self._count + 1

        self._stack.append((price, self._count))
        self._count += 1

        return span


class Solution:
    def largestRectangleAreaM1(self, heights: List[int]) -> int:
        """
        Largest Rectangle in Histogram
        Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

        Given an array of integers heights representing the histogram's
        bar height where the width of each bar is 1, return the area of
        the largest rectangle in the histogram.
        """
        # In this particular method, we take 3 passes of the
        # input and find the answer.
        n = len(heights)
        leftSmallest, rightSmallest = [-1] * n, [n] * n

        # Finding left smallest indexes
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                leftSmallest[i] = stack[-1]
            stack.append(i)

        # Finding right smallest indexes
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                rightSmallest[i] = stack[-1]
            stack.append(i)

        largestArea = float("-inf")
        for i in range(n):
            # Area = (rightIndex - 1 - (leftIndex - 1) - 1)
            area = (rightSmallest[i] - leftSmallest[i] - 1) * heights[i]
            largestArea = max(area, largestArea)

        # Type checking
        assert type(largestArea) is int
        return largestArea
