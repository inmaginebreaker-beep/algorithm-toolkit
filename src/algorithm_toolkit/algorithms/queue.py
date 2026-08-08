from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: deque[T] = deque()

    def is_empty(self) -> bool:
        return not self.items

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("cannot dequeue from an empty queue")

        return self.items.popleft()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("cannot peek an empty queue")

        return self.items[0]

    def size(self) -> int:
        return len(self.items)
