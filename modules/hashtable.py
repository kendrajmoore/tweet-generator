from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n^2), two loops  Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = [] # O(1) - constant time
        for bucket in self.buckets: # loop O(n)
            for key, value in bucket.items(): # O(n)
                all_keys.append(key)  # O(1)
        return all_keys  #O(1)

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n^2) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = [] # constant
        for bucket in self.buckets: # loop O(n)
            for key, value in bucket.items():# O(n)
                all_values.append(value) # O(1)
        return all_values # O(1)

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n), you make one loop through buckets Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = [] # constant
        for bucket in self.buckets: # loop O(n)
            all_items.extend(bucket.items()) 
        return all_items # O(1)

    def length(self):
        #I need help is this O(n ^ 2)
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        return sum(bucket.length() for bucket in self.buckets)


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(n), loop through linked list  Why and under what conditions?"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda kv: kv[0] == key)
        return entry is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(n), loop through the linked list to find value. O(1) if earlier node, Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        entry = bucket.find(lambda kv: kv[0] == key) #O(n)
        if entry is not None:
            return entry[1] 
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(n), loop through the linked list to find value. O(1) if earlier node"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index]  # O(1)
        entry = bucket.find(lambda kv: kv[0] == key) #O(n)
        if entry is not None:
            bucket.delete(entry) # O(1)
            self.size -= 1 # O(1)
        bucket.append((key, value))  # O(1)
        self.size += 1  # O(1)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        entry = bucket.find(lambda kv: kv[0] == key) #O(n)
        if entry is not None:
            bucket.delete(entry) # O(1)
            self.size -= 1 # O(1)
        else:
            raise KeyError('Key not found: {}'.format(key)) # O(1)


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()