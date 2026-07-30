class LinkedList:
    class Node:
        def __init__(self, data: int) -> None:
            self.data = data
            self.next: LinkedList.Node | None = None

    def __init__(self) -> None:
        self.head: LinkedList.Node | None = None

    def append(self, data: int) -> None:
        new_node = self.Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def prepend(self, data: int) -> None:
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key: int) -> bool:
        current_node = self.head
        previous_node: LinkedList.Node | None = None

        while current_node is not None:
            if current_node.data == key:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next

                return True

            previous_node = current_node
            current_node = current_node.next

        return False

    def search(self, key: int) -> bool:
        current_node = self.head

        while current_node is not None:
            if current_node.data == key:
                return True

            current_node = current_node.next

        return False

    def to_list(self) -> list[int]:
        result: list[int] = []
        current_node = self.head

        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next

        return result
