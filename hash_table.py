# Bradley Curci
# Monday, may 27, 2024

from bucket import Bucket
from abc import ABC

class HashTable(ABC):

    def __init__(self, size):
        self.__size = size
        self.__table = [[] for _ in range(0, size)]

    def get_size(self):
        return self.__size
    
    def set_table(self, index, value):
        self.__table[index].append(value)

    def get_table(self):
        return self.__table

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


    def insert(self, value):
        pass
    
    def search(self, value):
        pass

    def remove(self, value):
        pass
    
    