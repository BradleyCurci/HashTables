# Bradley Curci
# Monday, may 27, 2024

from bucket import Bucket
from abc import ABC

class HashTable(ABC):

    def __init__(self, size):
        self.__size = size
        self.__unique_keys = 0
        self.__collisions = 0
        self.__table = [[] for _ in range(size)]

    def get_size(self):
        return self.__size
    
    def get_table(self):
        return self.__table
    
    def get_unique_keys(self):
        return self.__unique_keys
    
    def get_collisions(self):
        return self.__collisions
    
    def set_table(self, index, value):
        self.__table[index].append(value)


    def __str__(self):
        string = f'Table {id(self)}\nSize: {self.__size}\nContents:\n'
        for list in self.__table:
            if len(list) > 0:
                for item in list:
                    string = string + '[' + str(item.get_value()) + '] '
                string  = string + '\n'
            else:
                string = string + '[]\n'

        return string


    # MARK: Mid-sqare hashing
    # Returns the key given a value
    def mid_square_hash(self, value):
        square = value * value
        square_str = str(square)
        
        num_digits = len(str(self.__size))
        mid_index = len(square_str) // 2
        
        if len(square_str) < num_digits:
            hash_value = int(square_str)
        else:
            start = max(0, mid_index - (num_digits // 2))
            end = start + num_digits
            
            # Ensure end does not exceed length of square_str
            if end > len(square_str):
                end = len(square_str)
                start = end - num_digits if end - num_digits >= 0 else 0

            hash_value = int(square_str[start:end])

        return hash_value % self.__size
    

    def modulo_hash(self, value):
        return value % self.__size


    def insert(self, bucket):
        hash_index = bucket.get_key()
        list_index_of_key = self.__table[hash_index]

        # Check if the key were inserting at is empty if so increase unique keys
        if len(list_index_of_key) == 0:
            self.__unique_keys += 1
        else:
            self.__collisions += 1

        list_index_of_key.append(bucket)
        

    
    def search(self, value):
        pass

    def remove(self, value):
        pass
    
    