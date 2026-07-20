class Stack:
    def __init__(self) -> None:
        self.items: list[int] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("不能从空栈中弹出元素")
        return self.items.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("空栈没有顶部元素")
        return self.items[-1]


    def size(self) -> int:
        return len(self.items)