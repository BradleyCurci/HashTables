# Bradley Curci
# Monday, May 27, 2024
# Bucket Class

class Bucket:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value
    
    def get_key(self):
        return self.__key

    def __str__(self):
        return f'Bucket {id(self)}:\nKey: {self.__key}\nValue: {self.__value}'