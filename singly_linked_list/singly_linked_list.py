class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def add_to_tail(self, value):
        # wrap the input value in a node 
        new_node = Node(value)
        # check if there is no head (i.e., set both head and tail to the )
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tails next referenceto our new node
            self.tail.set_next(new_node)
            # set the lists tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # return none if there is no head (i.e., the list is empty )
        if not self.head:
            return None

        # if head has no next, there is a single element in the linked list
        removed_value = self.head.get_value()
        # get a reference to the head 
        self.head = self.head.next
        # deletes the list head reference 
        if not self.head:
            #get a reference to the head 
            # make sure tail reference doesnt refer to anything
            self.tail = None
        return removed_value

    def remove_tail(self):
        if not self.head:
            return None

        curr = self.head
        prev = curr
        while curr.get_next() != None:
            prev = curr
            curr = curr.get_next()

        prev.set_next(None)
        self.tail = prev
        return curr

    def get_max(self):
        if not self.head:
            return None

        curr = self.head
        max_value = curr.get_value()
        while curr != None:
            max_value = max(max_value, curr.get_value())
            
            curr = curr.get_next()
        return max_value

    def contains(self, value):
        # get a reference to the node we're currently at; update this as we traverse the

        curr = self.head
        # get a reference to the node we're currently at; update this as we traverse the
        while curr != None:
            # return True if the current value we're lookin at matdhes out target value
            if curr.get_value() is value:
                return True
            # update our current node to the current node's next value
            curr = curr.get_next()
            # if we've gotten here, then the target node isn't in our list
        return False 