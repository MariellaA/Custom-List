from collections import deque
from typing import Any, Sequence


class CustomList:
    def __init__(self, *args):
        self.__list = [*args]

    def __check_index_validity(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be of type int")

        if not (0 <= index < len(self.__list)) and not (0 > index >= -len(self.__list)):
            raise ValueError("Index out of range")

    def __check_value_in_list(self, value):
        if value not in self.__list:
            raise ValueError("No such value in the list")

    def append(self, value):
        self.__list.append(value)

        return self.__list

    def remove(self, index):
        self.__check_index_validity(index)

        return self.__list.pop(index)

    def get(self, index):
        self.__check_index_validity(index)

        return self.__list[index]

    def extend(self, values: Sequence[Any]):
        # check if values is iterable -> "", set(), [], {}
        try:
            self.__list.extend(values)
            return self.__list
        except TypeError:
            raise ValueError(f"{values} is not iterable")

    def insert(self, index, value):
        self.__check_index_validity(index)
        self.__list.insert(index, value)

        return self.__list

    def pop(self):
        if len(self.__list) == 0:
            raise ValueError("List is empty")
        return self.__list.pop(-1)

    def clear(self):
        self.__list = []

    def index(self, value):
        self.__check_value_in_list(value)
        return self.__list.index(value)

    def count(self, value):
        return self.__list.count(value)

    def reversed(self):
        # returns the list reversed but doesn't actually change it
        return self.__list[::-1]

    def copy(self):
        return self.__list.copy()

    def size(self):
        return len(self.__list)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        result = {}

        for index in range(0, len(self.__list), 2):
            key = self.__list[index]
            try:
                value = self.__list[index + 1]
            except IndexError:
                value = ""

            result[key] = value

        return result

    def move(self, n):
        if not isinstance(n, int):
            raise ValueError(f"{n} is not a valid int")
        if n >= len(self.__list):
            raise ValueError("Nothing to move")

        first_part = self.__list[:n]
        second_part = self.__list[n:]

        self.__list = second_part + first_part

        return self.__list

    def move_left(self, n):
        if not isinstance(n, int):
            raise ValueError(f"{n} is not a valid int")
        if n >= len(self.__list):
            raise ValueError("Nothing to move")

        first_part = self.__list[n - 1:]
        last_index = len(self.__list) - n
        second_part = self.__list[:last_index]

        self.__list = first_part + second_part

        return self.__list

    def __return_element_or_length(self, el):
        try:
            return len(el)   # integers do not have len
        except TypeError:
            return el

    def sum(self):
        result = 0

        for el in self.__list:
            result += self.__return_element_or_length(el)

        return result


    def overbound(self):
        max_num = float("-inf")
        biggest_index = None

        for index in range(len(self.__list)):
            current_value = self.__return_element_or_length(self.__list[index])

            if max_num <= current_value:
                max_num = current_value
                biggest_index = index

        return biggest_index

    def underbound(self):
        min_num = float("inf")
        smallest_index = None

        for index in range(len(self.__list)):
            current_value = self.__return_element_or_length(self.__list[index])

            if min_num >= current_value:
                min_num = current_value
                smallest_index = index

        return smallest_index


cl = CustomList(1, 2, -3, "asd", [4, 5, 'asd', 7])
#
# print(cl.append(5))
# print(cl.remove(-4))

print(cl._CustomList__list)

# print(cl.get(-10))
# print(cl.get(""))
# print(cl.get(-1))

# print(cl.extend([1, 2]))
# print(cl.extend(5))
# print(cl.insert(1, 2))

# print(cl.pop())
# print(cl.pop())
# print(cl.pop())
# print(cl.pop())

# cl.clear()

# print(cl.index(5))
# print(cl.index(1))

# print(cl.count(1))
# print(cl.count(5))

# print(cl.reversed())

# print(id(cl._CustomList__list))
# print(id(cl.copy()))

# print(cl.dictionize())

# print(cl.move(3))
# print(cl.move(6))

# print(cl.sum())

print(cl.overbound())
print(cl.underbound())

print(cl._CustomList__list)


