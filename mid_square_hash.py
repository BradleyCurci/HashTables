# Bradley Curci
# Monday, May 27, 2024
from hash_table import HashTable
import math

class MidSquareHashTable(HashTable):

    def __init__(self, size):
        super().__init__(size)

    def insert(self, bucket):
        key = bucket.get_key() # Key = 
        N =  super().get_size() # N = Lenght of list
        R =  math.floor(math.log10(N))

        middle = 0

        try:
            key_squared = key * key
            middle = self.get_middle(R, key_squared)
        except ValueError:
            print(f"R value ({R}) calculated to be greater than the length of the table. ({N})")


        super().set_table(middle, bucket.get_value())

    def get_middle(self, R, N):
        string = str(N)
        length = len(string)

        if R > length:
            raise ValueError('R value larger than the length of the table.')

        start = (length - R) // 2

        return int(string[start:start + R])

    def get_key(self, value):
        return value % super().get_size()