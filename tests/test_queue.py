from dataclasses import dataclass

import pytest

from algorithm_toolkit.algorithms.queue import Queue


@dataclass
class User:
    name: str


def test_queue_starts_empty() -> None:
    queue = Queue[int]()

    assert queue.is_empty()
    assert queue.size() == 0


def test_enqueue_and_dequeue() -> None:
    queue = Queue[int]()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.is_empty()


def test_peek_does_not_remove_item() -> None:
    queue = Queue[int]()
    queue.enqueue(10)

    assert queue.peek() == 10
    assert queue.size() == 1


def test_dequeue_empty_queue_raises_error() -> None:
    queue = Queue[int]()

    with pytest.raises(IndexError, match="empty queue"):
        queue.dequeue()


def test_queue_supports_strings() -> None:
    queue = Queue[str]()

    queue.enqueue("alpha")
    queue.enqueue("beta")

    assert queue.dequeue() == "alpha"
    assert queue.peek() == "beta"


def test_queue_supports_custom_objects() -> None:
    queue = Queue[User]()

    alice = User(name="Alice")
    bob = User(name="Bob")

    queue.enqueue(alice)
    queue.enqueue(bob)

    assert queue.dequeue() == alice
    assert queue.peek() == bob
