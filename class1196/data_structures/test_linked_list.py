import unittest
from class1196.data_structures.linked_list import LinkedList, Node


class LinkedListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_list = LinkedList()

    def assertLinkedListEqual(self, l: list[object]) -> None:
        self.assertEqual(self.test_list.as_list(), l)


class LinkedListInsertionTest(LinkedListTest):
    def test_inserting_node_in_the_begining_of_an_empty_list(self) -> None:
        self.test_list.insert_begin(4)

        self.assertLinkedListEqual([4])

    def test_inserting_node_in_the_begining_of_a_list(self) -> None:
        self.test_list.insert_begin(1)
        self.test_list.insert_begin(4)
        self.test_list.insert_begin(6)

        self.assertLinkedListEqual([6, 4, 1])

    def test_inserting_node_in_the_end_of_an_empty_list(self) -> None:
        self.test_list.insert_end(78)

        self.assertLinkedListEqual([78])

    def test_inserting_node_in_the_end_of_a_list(self) -> None:
        self.test_list.insert_end(78)
        self.test_list.insert_end(79)
        self.test_list.insert_end(1)

        self.assertLinkedListEqual([78, 79, 1])

    def test_inserting_node_at_an_existing_position(self) -> None:
        self.test_list.insert_end(1)
        self.test_list.insert_end(2)
        self.test_list.insert_end(3)
        self.test_list.insert_end(4)

        self.test_list.insert_position(1, 89)

        self.assertLinkedListEqual([1, 2, 89, 3, 4])

    def test_inserting_node_at_non_existing_position(self) -> None:
        self.test_list.insert_position(39, 89)

        self.assertLinkedListEqual([])


class LinkedListRemovalTest(LinkedListTest):

    def test_removing_head_from_an_empty_list(self) -> None:
        self.test_list.remove_begin()

        self.assertLinkedListEqual([])

    def test_removing_head_from_a_list_with_one_element(self) -> None:
        self.test_list.insert_begin(1)

        self.test_list.remove_begin()

        self.assertLinkedListEqual([])

    def test_removing_last_item_from_an_empty_list(self) -> None:
        self.test_list.remove_end()

        self.assertLinkedListEqual([])

    def test_removing_last_item_from_a_list(self) -> None:
        self.test_list.insert_end(1)
        self.test_list.insert_end(2)
        self.test_list.insert_end(3)

        self.assertLinkedListEqual([1, 2, 3])

        self.test_list.remove_end()

        self.assertLinkedListEqual([1, 2])

    def test_removing_an_existing_position(self) -> None:
        self.test_list.insert_end(1)
        self.test_list.insert_end(2)
        self.test_list.insert_end(3)
        self.test_list.insert_end(4)

        self.assertLinkedListEqual([1, 2, 3, 4])

        self.test_list.remove_position(1)

        self.assertLinkedListEqual([1, 2, 4])

    def test_removing_non_existing_position(self) -> None:
        self.test_list.insert_end(1)
        self.test_list.insert_end(2)

        self.assertLinkedListEqual([1, 2])

        self.test_list.remove_position(3)

        self.assertLinkedListEqual([1, 2])

    def test_removing_position_from_empty_list(self) -> None:

        self.assertLinkedListEqual([])

        self.test_list.remove_position(4)

        self.assertLinkedListEqual([])


class LinkedListMiddleElementTest(LinkedListTest):
    def test_middle_element_of_an_empty_list(self) -> None:
        self.assertLinkedListEqual([])

        self.assertIsNone(self.test_list.middle())

    def test_middle_element_of_an_even_list(self) -> None:
        self.test_list.insert_end(1)
        self.test_list.insert_end(2)
        self.test_list.insert_end(3)
        self.test_list.insert_end(4)

        self.assertLinkedListEqual([1, 2, 3, 4])

        self.assertEqual(self.test_list.middle(), Node(3))

    def test_middle_element_of_an_odd_list(self) -> None:
        self.test_list.insert_end(10)
        self.test_list.insert_end(20)
        self.test_list.insert_end(300)
        self.test_list.insert_end(40)
        self.test_list.insert_end(50)

        self.assertLinkedListEqual([10, 20, 300, 40, 50])

        self.assertEqual(self.test_list.middle(), Node(300))


class LinkedListReversalTest(LinkedListTest):
    def test_reverse_an_empty_list(self) -> None:
        self.assertLinkedListEqual([])

        self.test_list.reverse()

        self.assertLinkedListEqual([])

        self.assertIsNone(self.test_list.head)

    def test_reverse_a_list_with_one_element(self) -> None:
        self.test_list.insert_begin(1)

        self.assertLinkedListEqual([1])

        self.test_list.reverse()

        self.assertLinkedListEqual([1])

        self.assertEqual(self.test_list.head, Node(1))

    def test_reverse_a_list(self) -> None:
        self.test_list.insert_end(1)
        self.test_list.insert_end(2)
        self.test_list.insert_end(3)

        self.assertLinkedListEqual([1, 2, 3])

        self.test_list.reverse()

        self.assertLinkedListEqual([3, 2, 1])

        self.assertEqual(self.test_list.head, Node(3))


if __name__ == "__main__":
    unittest.main()
