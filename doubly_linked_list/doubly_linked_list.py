"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    """
    Optional `delete` method on `ListNode` to make subsequent
    methods more DRY.
    """
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value, None, None)
        self.length += 1
        # check if the DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode(value, None, None)
        # increment the length 
        self.length += 1
        
        # if empty DLL
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        # if not empty DLL
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        # if DLL is empty, there is a nothing to delete, we should return
        if not self.head and not self.tail:
            return None
        # if DLL has one element, remove it by 
        # setting head and tail pointers to None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            # decrement length of DLL
            self.length -= 1
        # if node to delete is head,
        # set DLL head pointer to node.next
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        # if node to delete is tail
        # reset DLL tail pointer 
        # delete node connections
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        current_node = self.head
        max_value = self.head.value
        for i in range(1, self.length):
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value