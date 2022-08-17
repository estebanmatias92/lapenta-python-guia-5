from helpers.stdio.stdio import int_input


def input_list_int(message, condition):
    """Ask the user for integers to store in a list, until the condition is matched.

    Args:
        message (string): Phrase to show with the input() function
        condition (function): Expression that evaluates every iteration

    Returns:
        list: Collection of valued entered by the user
    """

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
    """Iterates over an array, evaluates a callback agains each element, and
    creates a new collection with each new value returned.

    Args:
        list (all): Collection of element to transform
        function (function): Expression called with each element of the collection

    Returns:
        all: New collection with transformed values
    """

    new_list = []

    for item in list:
        new_list.append(function(item))

    return new_list


def reduce_list_int(iterable, function, initializer=None):
    """Copy of reduce() method. Iterates a collection and evaluates each element against
    a callback, to merge, filter or reduce the values into a new single value.

    Args:
        iterable (collection): Collection to reduce
        function (function): Callback to use against each value from the collection
        initializer (all, None): First default value for the new reduced object. Defaults to None.

    Returns:
        all: New object left after cumulate, filter or reduce the list
    """

    it = iter(iterable)

    if initializer is None:
        value = next(it)
    else:
        value = initializer

    for element in it:
        value = function(value, element)

    return value


def find_max(list):
    """Copy of max(). It search for the maximun value in a list.

    Args:
        list (list): List of data from which to find the maximun value

    Returns:
        all: Maximun value founded
    """

    max_value = None

    for num in list:
        if max_value == None or num > max_value:
            max_value = num

    return max_value


def find_min(list):
    """Copy of min(). It search for the minimun value in a list.

    Args:
        list (list): List of data from which to find the minimun value

    Returns:
        all: Minimun value founded
    """

    min_value = None

    for num in list:
        if min_value == None or num < min_value:
            min_value = num

    return min_value


def split_int(num):
    """Split and integer into a list of integers.

    Args:
        num (int): Numeric input parameter to split

    Raises:
        ValueError: Thrown an error if the type is not numeric

    Returns:
        list<int>: Returns a list of one or multiple digits
    """

    if type(num) != int:
        raise ValueError("The value given is not an integer.")

    int_list = [int(item) for item in str(num)]

    return int_list
