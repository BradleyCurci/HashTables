# Bradley Curci
# Monday, May 27, 2024
from bucket import Bucket
from hash_table import HashTable
from mid_square_hash import MidSquareHashTable
import random

def get_number(upper):
    number = random.randint(0, upper)
    return number


if __name__ == "__main__":
    msTable = MidSquareHashTable(100)
    for i in range(0, 100):
        number = get_number(100)
        bucket = Bucket(msTable.get_key(number), number)
        msTable.insert(bucket)

    for list in msTable.get_table():
        print(list)
