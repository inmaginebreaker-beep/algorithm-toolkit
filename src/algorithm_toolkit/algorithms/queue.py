class Queue:
    def __init__(self) -> None:
        self.items: list[int] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item: int) -> None:
        self.items.append(item)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("cannot dequeue from an empty queue")

        return self.items.pop(0)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("cannot peek an empty queue")

        return self.items[0]

    def size(self) -> int:
        return len(self.items)
