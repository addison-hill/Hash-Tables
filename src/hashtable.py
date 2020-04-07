# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # hash mod the key to get our bucket
        index = self._hash_mod(key)

        # Check if a pair already exists in the bucket
        pair = self.storage[index]
        if pair == None:
            # create a new Linked Pair and place it in the bucket
            self.storage[index] = LinkedPair(key, value)
        else:
            while pair is not None:
                if pair.key == key:
                    # overwrite the value
                    pair.value = value
                    return
                elif pair.next == None:
                    # when you get to end create a new LinkedPair
                    pair.next = LinkedPair(key, value)
                    return
                else:
                    # iterate through the linked list
                    copy = pair
                    pair = copy.next

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None and self.storage[index].key == key:
            self.storage[index] = None
        else:
            print("WARNING: Key not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get the index from hashmod
        index = self._hash_mod(key)

        # check if a pair exists in the bucket with matching keys
        while self.storage[index]:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                # go to the next item in the Linked List
                self.storage[index] = self.storage[index].next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for bucket_item in old_storage:
            while bucket_item:
                self.insert(bucket_item.key, bucket_item.value)
                bucket_item = bucket_item.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    print(ht.storage)
    # ht.insert("key-0", "new-val-0")
    # print(ht.storage)
    # # print(ht.retrieve("key-0"))
    ht.resize()
    print(ht.storage)
    ht.resize()
    print(ht.storage)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print(ht.storage)

    # print("")

    # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
