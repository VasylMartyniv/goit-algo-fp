class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_linked_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.data < list2.data:
        result = list1
        result.next = merge_sorted_linked_lists(list1.next, list2)
    else:
        result = list2
        result.next = merge_sorted_linked_lists(list1, list2.next)

    return result


# Example of usage
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Creating two sorted linked lists
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

print("List 1:")
print_list(list1)

print("List 2:")
print_list(list2)

# Merging the two lists
merged_head = merge_sorted_linked_lists(list1, list2)

print("Merged list:")
print_list(merged_head)
