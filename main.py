# Bradley Curci
# Monday, May 27, 2024
from bucket import Bucket
from hash_table import HashTable
import time
import random

def get_number(lower, upper):
    number = random.randint(lower, upper)
    return number

# returns a list of random numbers between 0, size 
def get_number_list(length):
    return_list = []
    for i in range(length):
        print(f'Generating {length} sample values...   [{color_text(str(i + 1), 'blue')}/{color_text(str(length), 'blue')}]  {color_text(str(int((i + 1)/length * 100)), "green")}%', end="\r")
        return_list.append(get_number(0, length))
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
    print("Welcome to the B2U lesson on Hash Tables!")
    print("Please be sure to explore this program in its entirety before disecting the code.")
    print()

def print_progress_bar(current_iteration, total_iterations):
    total_length = 100


def print_storing_results(size, unique_keys, time, collisions):
    print()
    print(f'Successfully stored {color_text(str(size), 'blue')} values')
    print(f'{color_text(str(unique_keys), 'blue')} unique keys ({int((unique_keys / size) * 100)}% distribution)')
    print(f'{color_text(str(collisions), 'red')} collisions ({int((collisions / size) * 100)}% collison rate)')
    print(f'Time: {round((time * 1000), 4)} ms')
    print()



def mid_square_hashing(size):
    table = HashTable(size)

    # Create a list of random numbers
    values = get_number_list(size)

    # Create key, create, bucket, and insert bucket into table
    timer_start = time.time()
    for value in values:
        key = table.mid_square_hash(value)
        bucket = Bucket(key, value)
        table.insert(bucket)
    timer_end = time.time()
    time_length = timer_end - timer_start
    collisions = table.get_collisions()
    unique_keys = table.get_unique_keys()
    unique_keys_text = ''
    if unique_keys >= table.get_size() // 2:
        unique_keys_text = color_text(str(unique_keys), 'green')
    else:
        unique_keys_text = color_text(str(unique_keys), 'yellow')

    print_storing_results(size, unique_keys, time_length, collisions)

def modulo_hash(size):
    table = HashTable(size)

    values = get_number_list(size)

    timer_start = time.time()
    for value in values:
        key = table.modulo_hash(value)
        bucket = Bucket(key, value)
        table.insert(bucket)
    timer_end = time.time()
    time_length = timer_end - timer_start
    collisions = table.get_collisions()
    unique_keys = table.get_unique_keys()
    if unique_keys >= table.get_size() // 2:
        unique_keys_text = color_text(str(unique_keys), 'green')
    else:
        unique_keys_text = color_text(str(unique_keys), 'yellow')

    print_storing_results(size, unique_keys, time_length, collisions)



def select_demo():
    print("Select one of the following algorithms to run:")
    print('[1] Modulo Hash')
    print('[2] Mid-square hash')
    print('[3] Mid_square hash (base 2)')
    print('[4] Multiplicative String Hash')

    valid_input = False
    while not valid_input:
        selection = input()
        if not selection.isdigit():
            print("Selection must be of type integer.")
            continue
        else:
            selection = int(selection)

        if not 0 < selection < 5:
            print("Selection Must be between digits 1 - 4.")
            continue
        
        size = input("Please enter the length of data to generate: ")
        if not size.isdigit():
            print('Size must be of type integer.')
            continue
        else:
            size = int(size)
            valid_input = True

    if selection == 1:
        modulo_hash(size)
    elif selection == 2:
        mid_square_hashing(size)
    elif selection == 3:
        print("RUNNING MID_SQUARE HASH BASE 2")
    elif selection == 4:
        print('RUNNING MULTIPLICATIVE STRING HASH')

if __name__ == "__main__":

    print_banner()

    select_demo()

    
    

    

