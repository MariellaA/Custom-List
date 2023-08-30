from unittest import TestCase, main

from custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self) -> None:
        self.custom_list = CustomList(1, 2, 3)

    def test_append(self):
        self.assertEqual(3, self.custom_list.size())
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.append(5)

        self.assertEqual(4, self.custom_list.size())
        self.assertEqual([1, 2, 3, 5], result)
        self.assertEqual([1, 2, 3, 5], self.custom_list._CustomList__list)

    def test_remove_invalid_index_raises(self):
        self.assertFalse(100 in self.custom_list._CustomList__list)
        # index is not an int
        with self.assertRaises(ValueError) as ve:
            self.custom_list.remove("100")
        self.assertEqual("Index must be of type int", str(ve.exception))

        # Index is out of range
        with self.assertRaises(ValueError) as ve:
            self.custom_list.remove(100)
        self.assertEqual("Index out of range", str(ve.exception))

    def test_remove(self):
        # Index is valid
        self.assertIn(2, self.custom_list._CustomList__list)
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.remove(1)

        self.assertEqual(2, result)
        self.assertEqual([1, 3], self.custom_list._CustomList__list)

    def test_get_invalid_index_raises(self):
        self.assertFalse(100 in self.custom_list._CustomList__list)
        # index is not an int
        with self.assertRaises(ValueError) as ve:
            self.custom_list.get("100")
        self.assertEqual("Index must be of type int", str(ve.exception))

        # Index is out of range
        with self.assertRaises(ValueError) as ve:
            self.custom_list.get(100)
        self.assertEqual("Index out of range", str(ve.exception))

    def test_get(self):
        # Index is valid
        self.assertIn(2, self.custom_list._CustomList__list)
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.get(1)

        self.assertEqual(2, result)
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

    def test_extend_with_non_iterable_raises(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        with self.assertRaises(ValueError) as ve:
            self.custom_list.extend(5)

        self.assertEqual("5 is not iterable", str(ve.exception))
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

    def test_extend(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.extend([4, 5, 6])

        self.assertEqual([1, 2, 3, 4, 5, 6], result)
        self.assertEqual([1, 2, 3, 4, 5, 6], self.custom_list._CustomList__list)

    def test_insert_invalid_index_raises(self):
        self.assertFalse(100 in self.custom_list._CustomList__list)
        # index is not an int
        with self.assertRaises(ValueError) as ve:
            self.custom_list.insert("100", 2)
        self.assertEqual("Index must be of type int", str(ve.exception))

        # Index is out of range
        with self.assertRaises(ValueError) as ve:
            self.custom_list.insert(100, 2)
        self.assertEqual("Index out of range", str(ve.exception))

    def test_insert(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.insert(2, 100)

        self.assertEqual([1, 2, 100, 3], result)
        self.assertEqual([1, 2, 100, 3], self.custom_list._CustomList__list)

    def test_pop_no_elements_raises(self):
        cl = CustomList()

        self.assertEqual(0, len(cl._CustomList__list))

        with self.assertRaises(ValueError) as ve:
            cl.pop()
        self.assertEqual("List is empty", str(ve.exception))

        self.assertEqual(0, len(cl._CustomList__list))

    def test_pop(self):
        self.assertEqual(3, len(self.custom_list._CustomList__list))

        result = self.custom_list.pop()

        self.assertEqual(3, result)
        self.assertEqual(2, len(self.custom_list._CustomList__list))
        self.assertEqual([1, 2], self.custom_list._CustomList__list)

    def test_clear(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        self.custom_list.clear()

        self.assertEqual([], self.custom_list._CustomList__list)

    def test_index_invalid_value_raises(self):
        self.assertNotIn(5, self.custom_list._CustomList__list)

        with self.assertRaises(ValueError) as ve:
            self.custom_list.index(5)

        self.assertEqual("No such value in the list", str(ve.exception))

    def test_index(self):
        self.assertIn(1, self.custom_list._CustomList__list)
        self.assertEqual(1, self.custom_list._CustomList__list[0])

        result = self.custom_list.index(1)

        self.assertEqual(0, result)

    def test_count(self):
        # Test count 0
        self.assertNotIn(5, self.custom_list._CustomList__list)

        result = self.custom_list.count(5)

        self.assertEqual(0, result)

        # Test count
        self.assertIn(3, self.custom_list._CustomList__list)

        result = self.custom_list.count(3)

        self.assertEqual(1, result)

    def test_reverse(self):
        # Reverse elements and return new list
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        custom_list_id = id(self.custom_list._CustomList__list)

        result = self.custom_list.reversed()

        # List should not change
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        # Result is reversed list
        self.assertEqual([3, 2, 1], result)

        # Since it is a new list ids should be different
        reversed_list_id = id(result)
        self.assertNotEqual(custom_list_id, reversed_list_id)

    def test_copy(self):
        # Reverse elements and return new list
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        custom_list_id = id(self.custom_list._CustomList__list)

        result = self.custom_list.copy()

        # List should not change
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        # Result is reversed list
        self.assertEqual([1, 2,3], result)

        # Since it is a new list ids should be different
        copy_list_id = id(result)
        self.assertNotEqual(custom_list_id, copy_list_id)

    def test_size(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)
        self.assertEqual(3, len(self.custom_list._CustomList__list))

        result = self.custom_list.size()

        self.assertEqual(3, result)
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

    def test_add_first(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.add_first(100)

        self.assertEqual([100, 1, 2, 3], self.custom_list._CustomList__list)
        self.assertIsNone(result)

    def test_dictionize(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.dictionize()

        self.assertEqual({1: 2, 3: ""}, result)
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        #3 Test with even n

        cl = CustomList(1, 2, 3, 4)

        self.assertEqual([1, 2, 3, 4], cl._CustomList__list)

        result = cl.dictionize()

        self.assertEqual({1: 2, 3: 4}, result)
        self.assertEqual([1, 2, 3, 4], cl._CustomList__list)

    def test_move_invalid_n_tye(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        with self.assertRaises(ValueError) as ve:
            self.custom_list.move("a")

        self.assertEqual("a is not a valid int", str(ve.exception))

    def test_move_bigger_n_than_len_or_equal_raises(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)
        self.assertEqual(3, len(self.custom_list._CustomList__list))

        with self.assertRaises(ValueError) as ve:
            # Bigger than value of the length
            self.custom_list.move(4)

        self.assertEqual("Nothing to move", str(ve.exception))
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        with self.assertRaises(ValueError) as ve:
            # Value of the length
            self.custom_list.move(3)

        self.assertEqual("Nothing to move", str(ve.exception))
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

    def test_move(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.move(2)

        self.assertEqual([3, 1, 2], result)
        self.assertEqual([3, 1, 2], self.custom_list._CustomList__list)

    def test_move_left(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

        result = self.custom_list.move_left(2)

        self.assertEqual([2, 3, 1], result)
        self.assertEqual([2, 3, 1], self.custom_list._CustomList__list)

    def test_sum(self):
        # Num is higher value
        cl = CustomList(1, 2, 3, [1, 2], 4, "asd")
        self.assertEqual([1, 2, 3, [1, 2], 4, "asd"], cl._CustomList__list)

        result = cl.sum()

        self.assertEqual(15, result)
        self.assertEqual([1, 2, 3, [1, 2], 4, "asd"], cl._CustomList__list)

    def test_overbound(self):
        # Num is higher value
        cl = CustomList(1, 2, 3, 4, [1, 2], "asd")
        self.assertEqual([1, 2, 3, 4, [1, 2], "asd"], cl._CustomList__list)

        result = cl.overbound()

        self.assertEqual(3, result)
        self.assertEqual(4, cl._CustomList__list[3])
        self.assertEqual([1, 2, 3, 4, [1, 2], "asd"], cl._CustomList__list)

        # Iterable is the biggest

        cl = CustomList(1, 2, 3, [1, 2, 3, 4], "asd")
        self.assertEqual([1, 2, 3, [1, 2, 3, 4], "asd"], cl._CustomList__list)
        self.assertEqual([1, 2, 3, 4], cl._CustomList__list[3])

        result = cl.overbound()

        self.assertEqual(3, result)
        self.assertEqual([1, 2, 3, 4], cl._CustomList__list[3])
        self.assertEqual([1, 2, 3, [1, 2, 3, 4], "asd"], cl._CustomList__list)

    def test_underbound(self):
        # Num is higher value
        cl = CustomList(2, 3, 4, 1, [1, 2], "asd")
        self.assertEqual([2, 3, 4, 1, [1, 2], "asd"], cl._CustomList__list)
        self.assertEqual(1, cl._CustomList__list[3])

        result = cl.underbound()

        self.assertEqual(3, result)
        self.assertEqual(1, cl._CustomList__list[3])
        self.assertEqual([2, 3, 4, 1, [1, 2], "asd"], cl._CustomList__list)

        # Iterable is the biggest
        cl = CustomList(2, 3, 4, [1, 2], "asd")
        self.assertEqual([2, 3, 4, [1, 2], "asd"], cl._CustomList__list)
        self.assertEqual([1, 2], cl._CustomList__list[3])

        result = cl.underbound()

        self.assertEqual(3, result)
        self.assertEqual([1, 2], cl._CustomList__list[3])
        self.assertEqual([2, 3, 4, [1, 2], "asd"], cl._CustomList__list)


if __name__ == "__main__":
    main()
