from courses.first.linked_list.LinkedList import LinkedList, Node


def linked_list_sum(first, second):
    if first.len() != second.len():
        return LinkedList()

    head_first = first.head
    head_second = second.head
    new_list = LinkedList()

    while head_first is not None:
        sum_node = Node(head_first.value + head_second.value)
        new_list.add_in_tail(sum_node)

        head_first = head_first.next
        head_second = head_second.next

    return new_list
