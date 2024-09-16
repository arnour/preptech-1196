import unittest
from class1196.data_structures.queue import Queue, LinkedQueue


class QueueTest(unittest.TestCase):

    def test_first_in_first_out(self) -> None:
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(q.dequeue(), 1)

    def test_dequeue_empty_queue(self) -> None:
        q = Queue()

        self.assertIsNone(q.dequeue())

    def test_dequeue_til_queue_is_empty(self) -> None:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertIsNone(q.dequeue())
        self.assertTrue(q.is_empty())


class LinkedQueueTest(unittest.TestCase):

    def test_enqueue_items(self) -> None:
        q = LinkedQueue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertFalse(q.is_empty())
        self.assertEqual(q.front(), 1)

    def test_first_in_first_out(self) -> None:
        q = LinkedQueue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.as_list(), [1, 2, 3])

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertTrue(q.is_empty())

    def test_front_of_an_empty_queue(self) -> None:
        q = LinkedQueue()

        self.assertIsNone(q.front())

    def test_front_of_a_queue(self) -> None:
        q = LinkedQueue()
        q.enqueue(10)
        q.enqueue(20)

        self.assertEqual(q.front(), 10)
