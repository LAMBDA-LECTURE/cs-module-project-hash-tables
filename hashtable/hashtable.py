class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        ratio of items in the list vs how many spaces are in the list
            filled:potential capacity
        Implement this.
        """
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # algorithm fnv-1 :
        #     hash := FNV_offset_basis
        #     for each byte_of_data to be hashed do
        #         hash := hash × FNV_prime
        #         hash := hash XOR byte_of_data
            # return hash
        FNV_prime = 1099511628211
        FNV_offset = 14695981039346656037

        hash = FNV_offset
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # # Your code here
        # index = self.hash_index(key)
        # self.storage[index] = HashTableEntry(key, value)
        index = self.hash_index(key)
        node = HashTableEntry(key, value)
        #if there's something at that index:
        if self.storage[index] is not None:
            #& it has the same key we're given
            if self.storage[index].key == key:  # this and next 2 lines removable?
                #update the value
                self.storage[index].value = value
            else:
                #loop through the matching index's till we find the right value
                current = self.storage[index]
                while current.next is not None:
                    if current.key == key:
                        #& update that value
                        current.value = value
                    else:
                        #or keep looking
                        current = current.next
                #& if we reach the tail, which has no none, check it
                if current.key == key:
                    current.value = value
                #or add the value to this new node after the tail
                else:
                    current.next = node
                    self.size += 1
        #else if there's no matching indexes, just add the new node
        else:
            # when the index is none
            self.storage[index] = node
            self.size += 1
        if self.get_load_factor() >= .7:
            self.resize((self.capacity * 2))

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)
        # if not self.storage[index]:
        #     print("no key found")
        #     return

        # self.storage[index] = None

        index = self.hash_index(key)
        if self.storage[index] is None:
            #print a warning here
            return None
        #if the key matches at the first index
        elif self.storage[index].key == key: #possibly remove 145 - 153(until while loop) by including the head
            self.size -= 1
            #connect to the one after it if needed or just remove it
            if self.storage[index].next is not None:
                self.storage[index] = self.storage[index].next
            else:
                self.storage[index] = None
        #if there's multiple matching indexes
        else:
            prev = self.storage[index]
            current = self.storage[index].next
            while current is not None: # meat of it all
                if current.key == key:
                    prev.next = current.next
                    #do we actually need this next line??? I can't figure out why
                    # current.next = None
                    self.size -= 1
                else:
                    prev = current
                    current = current.next
            return "Nothing to see here"

    def get(self, key):
        """
        Retrieve the value stored with the given key
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)
        # if not self.storage[index]:
        #     return None

        # return self.storage[index].value

        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        current = self.storage[index]
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        for node in old_storage:
            if node is not None:
                self.put(node.key, node.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
