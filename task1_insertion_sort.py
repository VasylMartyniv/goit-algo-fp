class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, new_node):
    if head is None or head.data >= new_node.data:
        new_node.next = head
        head = new_node
    else:
        current = head
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return head


def insertion_sort_linked_list(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head


# Example of usage
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Creating a linked list 3 -> 1 -> 2 -> None
head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

print("Original list:")
print_list(head)

# Sorting the linked list
sorted_head = insertion_sort_linked_list(head)

print("Sorted list:")
print_list(sorted_head)
