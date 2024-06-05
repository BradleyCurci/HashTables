# Bradley Curci
# Monday, may 27, 2024

from bucket import Bucket
from abc import ABC

class HashTable(ABC):

    def __init__(self, size):
        self.__size = size
        self.__collisions = 0
        self.__table = [[] for _ in range(size)]

    def get_size(self):
        return self.__size
    
    def get_table(self):
        return self.__table
    
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

    def modulo_hash(self, value):
        ret_val = self.__size % value
        return ret_val
    

    def insert(self, bucket):
        hash_index = bucket.get_key()
        list_index_of_key = self.__table[hash_index]

        # Check if the key were inserting at is empty if so increase unique keys
        if len(list_index_of_key) != 0:
            self.__collisions += 1

        list_index_of_key.append(bucket)
    
    def calculate_distribution(self):
        occupied_bucket_count = 0
        for bucket in self.__table:
            if len(bucket) != 0:
                occupied_bucket_count +=1
        
        distribution = round((occupied_bucket_count / self.__size) * 100, 2)
        return distribution
    
    def search(self, search_value):
        key = self.modulo_hash(search_value)
        for i in range(len(self.__table[key])):
            if self.__table[key][i].get_value() == search_value:
                return (key, i)

    def remove(self, value):
        pass
    
    