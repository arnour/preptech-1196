from class1196.data_structures.linked_list import LinkedList, Node


# https://leetcode.com/problems/add-two-numbers/
def add_two_numbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    result = LinkedList()
    carry = 0
    num1, num2 = l1.head, l2.head
    while num1 or num2 or carry > 0:
        a, b = 0, 0
        if num1:
            a = num1.value
            num1 = num1.next
        if num2:
            b = num2.value
            num2 = num2.next
        val: int = a + b + carry
        carry: int = val // 10
        result.insert_end(val % 10)
    return result


# https://leetcode.com/problems/swap-nodes-in-pairs/description/
def swap_nodes_in_pairs(l1: LinkedList) -> LinkedList:
    if not l1.head or not l1.head.next:
        return l1
        
    result = LinkedList([0])
    head = l1.head
    dummy = result.head
    temp = dummy
    while head and head.next:
        cur = head.next.next # 3rd
        temp.next = head.next # 2nd
        temp = head # 1st
        head.next.next = head
        head.next = cur
        head = cur
    result.remove_begin()
    return result
        
