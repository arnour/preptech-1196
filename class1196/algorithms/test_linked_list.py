import unittest
from class1196.data_structures.linked_list import LinkedList
from class1196.algorithms.linked_list import add_two_numbers, swap_nodes_in_pairs


class AddTwoNumbersTest(unittest.TestCase):
    def test_add_two_numbers_of_same_order(self) -> None:
        l1 = LinkedList([2, 4, 3])

        l2 = LinkedList([5, 6, 4])

        result = add_two_numbers(l1, l2)

        self.assertEqual(result.as_list(), [7, 0, 8])

    def test_add_two_numbers_of_different_order(self) -> None:
        l1 = LinkedList([0, 0, 4])

        l2 = LinkedList([4])

        result = add_two_numbers(l1, l2)

        self.assertEqual(result.as_list(), [4, 0, 4])

    def test_add_two_numbers_zero(self) -> None:
        l1 = LinkedList([0])

        l2 = LinkedList([0])

        result = add_two_numbers(l1, l2)

        self.assertEqual(result.as_list(), [0])

    def test_add_two_numbers_move_carry_til_the_end(self) -> None:
        l1 = LinkedList([9, 9, 9, 9, 9, 9, 9])
        l2 = LinkedList([9, 9, 9, 9])

        result = add_two_numbers(l1, l2)

        self.assertEqual(result.as_list(), [8, 9, 9, 9, 0, 0, 0, 1])


class SwapNodesInPairsTest(unittest.TestCase):

    def test_swap_empty_list(self) -> None:
        l1 = LinkedList()

        l2 = swap_nodes_in_pairs(l1)

        self.assertEqual(l2.as_list(), [])

    def test_swap_one_node_list(self) -> None:
        l1 = LinkedList([1])

        l2 = swap_nodes_in_pairs(l1)

        self.assertEqual(l2.as_list(), [1])

    def test_swap_list(self) -> None:
        l1 = LinkedList([1, 2, 3, 4])

        l2 = swap_nodes_in_pairs(l1)

        self.assertEqual(l2.as_list(), [2, 1, 4, 3])
