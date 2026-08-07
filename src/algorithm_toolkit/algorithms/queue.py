from collections import deque


class Queue:
    def __init__(self) -> None:
        self.items: deque[int] = deque()

    def is_empty(self) -> bool:
        return not self.items

    def enqueue(self, item: int) -> None:
        self.items.append(item)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("cannot dequeue from an empty queue")

        return self.items.popleft()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("cannot peek an empty queue")

        return self.items[0]

    def size(self) -> int:
        return len(self.items)