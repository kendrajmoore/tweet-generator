class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

# ref https://medium.freecodecamp.org/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d
class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.list_length = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """O(1) because you only have to chec if the head node exists """
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """O(n) loop through the nodes to count the nodes. Return the length of this linked list by traversing its nodes."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1), we only change the last node(tail) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1), we never loop through all nodes Why and under what conditions?"""
        """As for time complexity, this implementation of insert is constant O(1) 
        (efficient!). This is because the insert method, no matter what, will always 
        take the same amount of time: it can only take one data point, it can only ever 
        create one node, and the new node doesn’t need to interact with all the other 
        nodes in the list, the inserted node will only ever interact with the head. """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item) # making a node
        # new_node.set_next(self.head)
        if self.head != None:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) If it is the first item, Why and under what conditions?
        TODO: Worst case running time: O(n) If you have to go through the entire list, Why and under what conditions?"""
        for data in self.items():
            if quality(data) is True:
                node = self.head
                while node is not None:
                    if node.data == data:
                        return node.data
                    node = node.next
                else:
                    continue
        return None
    

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1), the item can be in the front Why and under what conditions?
        TODO: Worst case running time: O(n) Why and under what conditions?"""
        """The time complexity for delete is also O(n), because in the worst 
        case it will visit every node, interacting with each node a fixed number of 
        times. """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.is_empty():
           raise ValueError("Item not found: {}".format(item))
        else:
            traversing = True
            previous_node = None
            current_node = self.head
            while traversing:
                if item == current_node.data:
                    if previous_node:
                        if self.tail == current_node:
                            previous_node.next = None
                            self.tail = previous_node
                        else:
                            previous_node.next = current_node.next
                    else:
                        if self.tail == self.head:
                            self.head = None
                            self.tail = None
                        else:
                            self.head = current_node.next
                    traversing = False
                    self.list_length -= 1
                else:
                    if current_node.next is None:
                        raise ValueError('Item not found: {}'.format(item))
                    else:
                        previous_node = current_node
                        current_node = current_node.next
            return current_node.data
        
       
       
       
        # previous = None
        # found = False
        # node = self.head
        # while not found and node is not None:
        #     if node.data == item:
        #         if previous is not None:
        #             previous.next = node.next
        #         else:
        #             self.head = node.next
        #         if node.next is None:
        #             self.tail = previous
        #         found = True
        #     previous = node
        #     node = node.next
        #     if not found:
        #         raise ValueError('Item not found: {}'.format(item))




def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()