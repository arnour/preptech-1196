import unittest
from class1196.data_structures.stack import Stack


class StackTest(unittest.TestCase):

    def test_last_in_first_out(self) -> None:
        s = Stack()

        s.push(1)
        s.push(2)

        self.assertEqual(s.pop(), 2)

    def test_popping_every_item(self) -> None:
        s = Stack()

        s.push(1)
        s.push(2)
        s.push(3)

        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertIsNone(s.pop())
        self.assertTrue(s.is_empty())

    def test_return_top(self) -> None:
        s = Stack()

        s.push(1)
        s.push(2)
        s.push(3)

        self.assertEqual(s.top(), 3)

    def test_return_top_as_None_if_empty(self) -> None:
        s = Stack()

        self.assertIsNone(s.top())
        self.assertTrue(s.is_empty())
