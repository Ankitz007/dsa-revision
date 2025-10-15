class Solution:
    def bracketNumbers(self, string):
        """
        Print Bracket Number
        Link: https://www.geeksforgeeks.org/problems/print-bracket-number4058/1

        Given a string str, the task is to find the bracket numbers,
        i.e., for each bracket in str, return i if the bracket is
        the ith opening or closing bracket to appear in the string.
        """
        count = 0
        stack, result = [], []

        for char in string:
            if char == "(":
                count += 1
                stack.append(count)
                result.append(count)
            elif char == ")":
                result.append(stack.pop())
        return result

    # Method 1
    def nextLargerElementM1(self, arr):
        """
        Next Greater Element
        Link: https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1

        You are given an array arr[] of integers, the task is to find the
        next greater element for each element of the array in order of
        their appearance in the array. Next greater element of an element
        in the array is the nearest element on the right which is greater
        than the current element.
        If there does not exist next greater of current element, then next
        greater element for current element is -1.
        """
        result = [-1] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                index = stack.pop()
                result[index] = arr[i]
            stack.append(i)
        return result

    # Method 2
    def nextLargerElementM2(self, arr):
        n = len(arr)
        result, stack = [-1] * n, []
        # We traverse the input in reverse order
        for i in range(n - 1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(arr[i])
        return result

    def leftSmaller(self, arr):
        """
        Smaller on left
        Link: https://www.geeksforgeeks.org/problems/smallest-number-on-left3403/1

        Given an array arr[] of integers, for each element in the array,
        find the nearest smaller element on its left. If there is no
        such smaller element, return -1 for that position.
        """
        n = len(arr)
        result = [-1] * n
        stack = []

        # Similar to the last one except we need to start
        # from the end in this one!
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                result[stack.pop()] = arr[i]
            stack.append(i)
        return result

    def nextGreaterCircular(self, arr):
        """
        Next Greater Element in Circular Array
        Link: https://www.geeksforgeeks.org/problems/next-greater-element/1

        Given a circular integer array arr[], the task is to determine
        the next greater element (NGE) for each element in the array.

        The next greater element of an element arr[i] is the first
        element that is greater than arr[i] when traversing circularly.
        If no such element exists, return -1 for that position.

        Note: Since the array is circular, after reaching the last
        element, the search continues from the beginning until we
        have looked at all elements once.
        """
        n = len(arr)
        result, stack = [-1] * n, []
        for i in range(2 * n):
            while stack and arr[stack[-1]] < arr[i % n]:
                result[stack.pop()] = arr[i % n]
            # This is a neat one to only push indexes
            # in the stack in first pass. Clever!
            if i < n:
                stack.append(i % n)
        return result

    def calculateSpan(self, arr):
        """
        Stock Span Problem
        Link: https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

        The stock span problem is a financial problem where we have a
        series of daily price quotes for a stock and we need to calculate
        the span of stock price for all days.
        You are given an array arr[] representing daily stock prices,
        the stock span for the i-th day is the number of consecutive days
        up to day i (including day i itself) for which the price of the
        stock is less than or equal to the price on day i. Return the
        span of stock prices for each day in the given sequence.
        """
        n = len(arr)
        result, stack = [1] * n, []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                result[idx] = idx - i
            stack.append(i)

        while stack:
            idx = stack.pop()
            result[idx] = idx + 1
        return result
