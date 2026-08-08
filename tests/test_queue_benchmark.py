from pytest_benchmark.fixture import BenchmarkFixture

from algorithm_toolkit.algorithms.queue import Queue


def test_queue_dequeue_benchmark(
    benchmark: BenchmarkFixture,
) -> None:
    def run() -> None:
        queue = Queue[int]()

        for number in range(10_000):
            queue.enqueue(number)

        while not queue.is_empty():
            queue.dequeue()

    benchmark(run)
