class Solution:
    def findMaxRow(self, mat, n):
        """
        Binary matrix having maximum number of 1s
        Link: https://www.geeksforgeeks.org/problems/binary-matrix-having-maximum-number-of-1s--170647/1

        Given a binary matrix (containing only 0 and 1) of order NxN.
        All rows are sorted already, We need to find the row number
        with the maximum number of 1s. Also, find the number of 1s in
        that row.

        Note:
            1. In case of a tie, print the smaller row number.
            2. Row number should start from 0th index.
        """

        def binarySearch(arr, m):
            m = len(arr)
            left, right = 0, m
            while left < right:
                mid = left + right >> 1
                if arr[mid] == 1:
                    right = mid
                else:
                    left = mid + 1
            return m - left

        result = [-1, -1]
        for i in range(n):
            num_ones = binarySearch(mat[i], n)
            if num_ones > result[1]:
                result = [i, num_ones]
        return result

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search a 2D Matrix
        Link: https://leetcode.com/problems/search-a-2d-matrix/description/

        You are given an m x n integer matrix matrix with the following
        two properties:
        - Each row is sorted in non-decreasing order.
        - The first integer of each row is greater than the last integer
          of the previous row.

        Given an integer target, return true if target is in matrix or
        false otherwise.
        """
        n, m = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // m, mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # This is not exactly a "binary search" question per say, but the intuition
    # that we start from either top-right or lower-left corners comes from
    # binary search concepts.
    #
    # Standing at top-left or lower-right corner, we see that values in both
    # rows and columns are either increasing or decreasing.
    # But standing at top-right or lower-left corners, we can see that rows
    # and columns are either in strictly increasing or decreasing order.
    #
    # Thi monotocity suggests us that we can use these corners as sort of "mid"
    # we use in binary search and eliminate respective rows and columns
    # effectively in a single iteration. That's basicall binary search!
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search a 2D Matrix II
        Link: https://leetcode.com/problems/search-a-2d-matrix-ii/description/

        Write an efficient algorithm that searches for a value target in an
        m x n integer matrix matrix. This matrix has the following properties:
        - Integers in each row are sorted in ascending from left to right.
        - Integers in each column are sorted in ascending from top to bottom.
        """
        rows, cols = len(matrix), len(matrix[0])
        x, y = 0, cols - 1

        while x < rows and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1

        return False

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        Find a Peak Element II
        Link: https://leetcode.com/problems/find-a-peak-element-ii/description/

        A peak element in a 2D grid is an element that is strictly
        greater than all of its adjacent neighbors to the left,
        right, top, and bottom.

        Given a 0-indexed m x n matrix mat where no two adjacent
        cells are equal, find any peak element mat[i][j] and return
        the length 2 array [i,j].

        You may assume that the entire matrix is surrounded by an
        outer perimeter with the value -1 in each cell.
        """

        def maxRowIndex(row):
            element, index = row[0], 0
            for i in range(1, len(row)):
                if row[i] > element:
                    element = row[i]
                    index = i
            return element, index

        rows, cols = len(mat), len(mat[0])
        left, right = 0, rows - 1

        while left <= right:
            mid = left + (right - left) // 2
            row_max, row_max_idx = maxRowIndex(mat[mid])

            top = mat[mid - 1][row_max_idx] if mid - 1 >= 0 else -1
            bottom = mat[mid + 1][row_max_idx] if mid + 1 < rows else -1

            if top < row_max > bottom:
                return [mid, row_max_idx]
            elif mid - 1 >= 0 and top > row_max:
                right = mid - 1
            else:
                left = mid + 1
        # Unreachable due to problem constraints
        return [-1, -1]

    def median(self, mat):
        """
        Median in a row-wise sorted Matrix
        Link: https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

        Given a row-wise sorted matrix mat[][] of size n*m, where
        the number of rows and columns is always odd. Return the
        median of the matrix.
        """

        def upperBound(nums, target):
            """
            Find the index of the first element greater than target
            in sorted list "nums".

            If no such element exists, returns len(arr).
            """
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left

        # We find all the values smaller than or equal to the possible median
        # for each row and then sum them up.
        #
        # Our main feasibility condition is that if a number is a
        # possible median for a matrix containing an odd number of elements,
        # then it will be the first element where the count of elements
        # smaller than or equal to it is greater than (total_elements // 2).
        def isPossibleMedian(possible_median, min_freq):
            freq = 0
            for row in mat:
                freq += upperBound(row, possible_median)
            return freq > min_freq

        rows, cols = len(mat), len(mat[0])
        min_freq = (rows * cols) // 2

        # The min and max values in the matrix are needed
        # since the matrix is just row wise sorted.
        min_val = min(row[0] for row in mat)
        max_val = max(row[-1] for row in mat)

        left, right = min_val, max_val
        while left < right:
            mid = left + (right - left) // 2
            if isPossibleMedian(mid, min_freq):
                right = mid
            else:
                left = mid + 1
        return left
