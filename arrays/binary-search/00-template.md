# Binary Search Pattern: Quick Guide

## Template 1: Finding the "Lower Bound": First Occurrence

This template is typically used to find the first element that meets a certain criteria. Think of it as a cautious search.

For example, finding the first 'True' in an array like [F, F, F, T, T, T]

```python
def lower_bound(arr: list, condition) -> int:
    """
    Finds the index of the first element for which condition(element) is True.
    """
    # `right` is exclusive, representing the first index NOT in the search.
    # The search space is [left, right).
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        # Check if the element at `mid` satisfies the condition.
        if condition(arr[mid]):
            # `mid` is a potential answer, but the FIRST one might be
            # to the left. We keep `mid` in our search space.
            right = mid
        else:
            # `mid` does not satisfy the condition, so the first
            # valid answer must be to the right of `mid`.
            left = mid + 1

    # The loop terminates when `left` and `right` converge at the
    # index of the first element that satisfies the condition.
    return left
```

**Behavior:** When mid is a potential answer, you keep it in the search space (right = mid) and try to find an even better (earlier) one.

**Result:** The loop converges with left pointing directly at the first element that satisfies the condition.

## Template 2: Finding the "Upper Bound": Last Occurrence

This template is used to find the last element that meets a criteria. Think of it as an aggressive search.

For example, finding the last 'True' in an array like [T, T, T, F, F, F]

```python
def upper_bound(arr: list, condition) -> int:
    """
    Finds the index of the last element for which condition(element) is True.
    """
    # `right` is exclusive, representing the first index NOT in the search.
    # The search space is [left, right).
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        # Check if the element at `mid` satisfies the condition.
        if condition(arr[mid]):
            # `mid` is a potential answer, but a later one might exist.
            # We aggressively search to the right of `mid`.
            left = mid + 1
        else:
            # `mid` does not satisfy the condition, so the boundary
            # must be at `mid` or to its left.
            right = mid

    # The loop pushes `left` to the first index that FAILS the condition.
    # Therefore, the last valid element is at `left - 1`.
    return left - 1
```

**Behavior:** When mid is a potential answer, you discard it (left = mid + 1) to aggressively search for a better (later) one.

**Result:** This pushes left just past the boundary of valid answers. It ends up pointing to the first element that fails the condition. Therefore, you must return left - 1 to get the last valid element.

## Common Mistake Patterns

### ❌ Wrong Pattern

```python
while left <= right:  # Will cause infinite loop!
    mid = (left + right) // 2
    if condition:
        right = mid      # Problem: when left==right==mid
    else:
        left = mid + 1
```

**Problem**: When `left == right == mid`, setting `right = mid` doesn't change anything → infinite loop
