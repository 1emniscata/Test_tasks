"""This module can find the first repetitive value in a provided list."""


def find_repetition(test_list):
    """Receives a list of values and returns the first repeating element."""

    new_list = []
    for element in test_list:
        if element not in new_list:
            new_list.append(element)
        else:
            return element


if __name__ == '__main__':
    example = ['a', 'b', 'c', 'd', 'c']
    print(f'The first repeating element: {find_repetition(example)}')
