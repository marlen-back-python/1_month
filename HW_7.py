'''3 FUNCTION'''
def nearest_number(numbers, num_used):
    numbers_sorted = sorted(numbers, key=lambda x: abs(x - num_used))
    return (num_used, numbers_sorted)

print(nearest_number([312, 996, 31, 1991], 1000))
print(nearest_number([5, 20.18, 103, 4], 27))


def get_i_by_index(iterable):
    while True:
        try:
            index = input(f'Enter an index from 1 to {len(iterable)} or "exit" to exit: ')
            if index.lower() == 'exit':
                break
            index = int(index)
            print(iterable[index - 1])
        except ValueError:
            print("Please enter an integer!\n")
        except IndexError:
            print(f"Index is out of range, try entering from 1 to {len(iterable) - 1}.\n")
get_i_by_index([12, 23, 43, 67, 908, 347, 15.5])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
division_number = list(filter(lambda x: x % 2 != 0, numbers))
print(division_number)


numbers = [1, 2, 3, 4, 5]
plus_number = list(map(lambda x: x+10, numbers))
print(plus_number)
