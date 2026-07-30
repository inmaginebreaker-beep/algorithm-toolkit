import pytest

from algorithm_toolkit.algorithms.queue import Queue


def test_queue_starts_empty() -> None:
    queue = Queue()

    assert queue.is_empty()
    assert queue.size() == 0


def test_enqueue_and_dequeue() -> None:
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.is_empty()


def test_peek_does_not_remove_item() -> None:
    queue = Queue()
    queue.enqueue(10)

    assert queue.peek() == 10
    assert queue.size() == 1


def test_dequeue_empty_queue_raises_error() -> None:
    queue = Queue()

    with pytest.raises(IndexError, match="empty queue"):
        queue.dequeue()