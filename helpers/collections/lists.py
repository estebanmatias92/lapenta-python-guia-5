from helpers.stdio.stdio import int_input


def input_list_int(message, condition):
    list = []

    while True:
        try:
            number = int_input(message)
        except ValueError as e:
            print(e)
            print("")
        else:
            if condition(number) == False:
                break
            list.append(number)

    return list


def filter_list_int(list, function):
    """Iterates over every item in the list, evaluating them agains fn expression
    if matches the criteria, the item is stored in a new list.
    At the end the list is returned, with or without items.


    Args:
        list (list<int>): List of integers to filtrate
    fn (function): Callback with an expression to check agains every item in
    the list

    Returns:
        list<int>: Returns a list full of items than matches the fn criteria, or
    an empty list otherwise
    """

    new_list = []

    for item in list:
        if function(item):
            new_list.append(item)

    return new_list


def map_list_int(list, function):
    new_list = []

    for item in list:
        new_list.append(function(item))

    return new_list


def reduce_list_int(iterable, function, initializer=None):
    it = iter(iterable)

    if initializer is None:
        value = next(it)
    else:
        value = initializer

    for element in it:
        value = function(value, element)

    return value


def find_max(list):

    max_value = None

    for num in list:
        if max_value == None or num > max_value:
            max_value = num

    return max_value


def find_min(list):

    min_value = None

    for num in list:
        if min_value == None or num < min_value:
            min_value = num

    return min_value


def split_int(num):

    if type(num) != int:
        raise ValueError("The value given is not an integer.")

    int_list = [int(item) for item in str(num)]

    return int_list
