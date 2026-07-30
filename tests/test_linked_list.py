from algorithm_toolkit.algorithms.linked_list import LinkedList


def test_append() -> None:
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)

    assert linked_list.to_list() == [10, 20]


def test_prepend() -> None:
    linked_list = LinkedList()

    linked_list.append(20)
    linked_list.prepend(10)

    assert linked_list.to_list() == [10, 20]


def test_search_existing_value() -> None:
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)

    assert linked_list.search(20)


def test_search_missing_value() -> None:
    linked_list = LinkedList()
    linked_list.append(10)

    assert not linked_list.search(99)


def test_delete_existing_value() -> None:
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    deleted = linked_list.delete(20)

    assert deleted
    assert linked_list.to_list() == [10, 30]


def test_delete_missing_value() -> None:
    linked_list = LinkedList()
    linked_list.append(10)

    deleted = linked_list.delete(99)

    assert not deleted
    assert linked_list.to_list() == [10]
