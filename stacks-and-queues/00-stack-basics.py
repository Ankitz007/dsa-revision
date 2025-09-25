from typing import Generic, TypeVar

T = TypeVar("T")


# Note the use of generics in python, neat!
class ArrayStack(Generic[T]):
    def __init__(self, capacity: int):
        self._capacity: int = capacity
        self._list: list[T | None] = [None] * self._capacity
        self._top: int = -1

    def push(self, value: T) -> None:
        if self.isFull():
            raise OverflowError("stack is full...")
        self._top += 1

        self._list[self._top] = value

    def pop(self) -> T:
        if self.isEmpty():
            raise ValueError("stack is empty...")
        element = self._list[self._top]
        assert element is not None
        self._list[self._top] = None  # Optional cleanup
        self._top -= 1
        return element

    def top(self) -> T:
        if self.isEmpty():
            raise ValueError("stack is empty...")
        element = self._list[self._top]
        assert element is not None
        return element

    def size(self) -> int:
        return self._top + 1

    def isEmpty(self) -> bool:
        return self._top == -1

    def isFull(self) -> bool:
        return self._top == self._capacity - 1


# Definition of a ListNode
class ListNode(Generic[T]):
    # Check out the syntax of defining the type hint for `next`!
    def __init__(self, data: T, next_node: "ListNode[T] | None" = None):
        self.data: T = data
        self.next: "ListNode[T] | None" = next_node


class LinkedListStack(Generic[T]):
    def __init__(self):
        self._size: int = 0
        self._top: ListNode[T] | None = None

    def push(self, value: T) -> None:
        self._top = ListNode(value, self._top)
        self._size += 1

    def pop(self) -> T:
        if self._top is None:
            raise ValueError("stack is empty...")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def top(self) -> T:
        if self._top is None:
            raise ValueError("stack is empty...")
        return self._top.data

    def size(self) -> int:
        return self._size

    def isEmpty(self) -> bool:
        return self._top is None
