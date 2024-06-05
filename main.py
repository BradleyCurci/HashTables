# Bradley Curci
# Monday, May 27, 2024
from bucket import Bucket
from hash_table import HashTable
import time
import random

global search_value

def get_number(lower, upper):
    number = random.randint(lower, upper)
    return number

# returns a list of random numbers between 0, size 
def get_number_list(length):
    global search_value
    return_list = []
    
    # Random number describing the index of a value that will later be used for searching.
    # if index i matches the search number index, we will later search for whatever number was generated at that index
    search_number_index = get_number(1, length)
    for i in range(length):
        number = get_number(0, length)
        if i == search_number_index:
            search_value = number
        print(f'Generating {length} sample values...   [{color_text(str(i + 1), 'blue')}/{color_text(str(length), 'blue')}]  {color_text(str(int((i + 1)/length * 100)), "green")}%', end="\r")
        return_list.append(number)
    print()
    return return_list

def color_text(text, color):
    color_code = color_codes.get(color, '0')
    return f'\033[{color_code}m{text}\033[0m'

color_codes = {
    'reset': '0',
    'black': '30',
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'magenta': '35',
    'cyan': '36',
    'white': '37'
}


# Printing attributes
def print_banner():
    text = 'HASH TABLES'
    text_length = len(text)
    print()
    print(''.join("=" for _ in range(30)))
    print(''.join(" " for _ in range(int((30 / 2) - (text_length / 2)))) + text)
    print(''.join("=" for _ in range(30)))
    print()
    print("Welcome to the C2U demonstration on Hash Tables!")
    print("Please be sure to explore this program in its entirety before disecting the code.")
    print("To quit the program, enter 'exit' when prompted to enter a size.")
    print()

def print_storing_results(size, time, distribution, collisions):
    print()
    print(f'Successfully stored {color_text(str(size), 'blue')} values')
    print(f'Collisions: {collisions} ({round(((collisions / size) * 100), 2)}%)')
    print(f'Time: {round((time*1000), 4)} ms')
    print(f'Distribution: {distribution}%')
    print()
    
def print_searching_results(value, key, index, time):
    print()
    print(f'Successfull located value {color_text(str(value), 'blue')}')
    print(f'Key: {key}')
    print(f'Index: {index}')
    print(f'Time: {round(time*1000, 4)} ms')
    print()
    
def modulo_hash(size):
    global search_value
    
    table = HashTable(size)

    values = get_number_list(size)

    timer_start_store = time.perf_counter()
    for value in values:
        key = table.modulo_hash(value)
        bucket = Bucket(key, value)
        table.insert(bucket)
    timer_end_store = time.perf_counter()
    distribution = table.calculate_distribution()
    time_length_store = timer_end_store - timer_start_store
    collisions = table.get_collisions()

    print_storing_results(size, time_length_store, distribution, collisions)
    
    print(f'Searching for: {search_value}')
    
    timer_start_search = time.perf_counter()
    
    key, index = table.search(search_value)
    
    timer_end_search = time.perf_counter()
    
    timer_length_search = timer_end_search - timer_start_search
    
    print_searching_results(search_value, key, index, timer_length_search)
    

def get_user_input():
    
    valid_size = False
    
    while not valid_size:
        size = input('Enter an amount of data to generate: ')
        
        if size == 'exit':
            return 'exit'

        if not size.isdigit():
            print('Input must be of type int. Try again.')
            continue
        
        size = int(size)
        
        
        if size > 500000:
            print("We advise against generating more than 500,000 data points as it may incur stress on your system.")
            
            valid_choice = False
            while not valid_choice:
                user_choice = input('Would you like to continue? (y/n): ')
                
                if user_choice.lower() == 'y':
                    valid_choice = True
                    valid_size = True
                elif user_choice.lower() == 'n':
                    valid_choice = True
                else:
                    print(f"Unrecognized character '{user_choice}'. Try agian.")
        else:
            valid_size = True
    
    return size
        
        

if __name__ == "__main__":

    print_banner()
    
    exit = False
    while not exit:
        user_size = get_user_input()
        if user_size == 'exit':
            exit = True
            continue
        
        modulo_hash(user_size)

    
    

    

