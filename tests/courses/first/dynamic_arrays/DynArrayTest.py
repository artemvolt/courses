import unittest

from courses.first.dynamic_arrays.DynArray import DynArray


class DynArrayTest(unittest.TestCase):

    def test_append(self):
        dyn = DynArray()

        for i in range(1, 17):
            dyn.append(1)

        self.assertEqual(16, len(dyn))
        self.assertEqual(16, dyn.count)
        self.assertEqual(16, dyn.capacity)

        dyn.append(1)
        self.assertEqual(17, len(dyn))
        self.assertEqual(17, dyn.count)
        self.assertEqual(32, dyn.capacity)

    def test_insert(self):
        dyn = DynArray()

        self.assertRaises(IndexError, dyn.insert, 32, 1)
        self.assertRaises(IndexError, dyn.insert, 1, 1)

        # [1]
        dyn.insert(0, 1)

        self.assertEqual(1, dyn.count)
        self.assertEqual(1, len(dyn))
        self.assertEqual(1, dyn[0])

        # [1,2]
        dyn.insert(1, 2)
        self.assertEqual(2, dyn.count)
        self.assertEqual(2, len(dyn))
        self.assertEqual(1, dyn[0])
        self.assertEqual(2, dyn[1])

        # [1,2,3]
        dyn.insert(2, 3)
        self.assertEqual(3, dyn.count)
        self.assertEqual(3, len(dyn))
        self.assertEqual(1, dyn[0])
        self.assertEqual(2, dyn[1])
        self.assertEqual(3, dyn[2])

        # [1, 4, 2, 3]
        dyn.insert(1, 4)
        self.assertEqual(4, dyn.count)
        self.assertEqual(4, len(dyn))
        self.assertEqual(1, dyn[0])
        self.assertEqual(4, dyn[1])
        self.assertEqual(2, dyn[2])
        self.assertEqual(3, dyn[3])

        # [1, 5, 4, 2, 3]
        dyn.insert(1, 5)
        self.assertEqual(5, dyn.count)
        self.assertEqual(5, len(dyn))
        self.assertEqual(16, dyn.capacity)
        self.assertEqual(1, dyn[0])
        self.assertEqual(5, dyn[1])
        self.assertEqual(4, dyn[2])
        self.assertEqual(2, dyn[3])
        self.assertEqual(3, dyn[4])

    def test_insert_with_more_capacity(self):
        dyn = DynArray()

        for i in range(1, 17):
            dyn.append(i)

        self.assertEqual(16, len(dyn))
        dyn.insert(1, 105)

        self.assertEqual(17, len(dyn))
        self.assertEqual(17, dyn.count)
        self.assertEqual(32, dyn.capacity)
        self.assertEqual(1, dyn[0])
        self.assertEqual(105, dyn[1])
        self.assertEqual(2, dyn[2])
        self.assertEqual(3, dyn[3])
        self.assertEqual(4, dyn[4])

    def test_delete_empty(self):
        dyn = DynArray()
        with self.assertRaises(IndexError):
            dyn.delete(0)

    # noinspection PyStatementEffect
    def test_delete(self):

        dyn = DynArray()
        self.assertRaises(IndexError, dyn.delete, 1)

        dyn.append(1)
        dyn.delete(0)
        self.assertEqual(0, len(dyn))
        self.assertEqual(16, dyn.capacity)
        self.assertEqual(0, dyn.count)
        self.assertEqual(16, dyn.capacity)
        with self.assertRaises(IndexError):
            dyn[0]

        dyn.append(1)
        dyn.append(2)

        # 2
        dyn.delete(0)
        self.assertEqual(1, len(dyn))
        self.assertEqual(2, dyn[0])
        self.assertEqual(16, dyn.capacity)

        # 2, 1
        dyn.append(1)

        # 2
        dyn.delete(1)
        self.assertEqual(1, len(dyn))
        self.assertEqual(2, dyn[0])
        self.assertEqual(16, dyn.capacity)

        # 2, 3, 4
        dyn.append(3)
        dyn.append(4)

        # 2, 4
        dyn.delete(1)
        self.assertEqual(2, len(dyn))
        self.assertEqual(2, dyn[0])
        self.assertEqual(4, dyn[1])
        self.assertEqual(16, dyn.capacity)

    def test_delete_with_more_capacity_min(self):

        dyn = DynArray()
        for i in range(1, 18):
            dyn.append(i)

        self.assertEqual(32, dyn.capacity)
        dyn.delete(0)
        dyn.delete(1)

        self.assertEqual(21, dyn.capacity)
        self.assertEqual(15, dyn.count)

        dyn.delete(0)
        dyn.delete(1)
        dyn.delete(2)
        dyn.delete(3)
        dyn.delete(4)

        self.assertEqual(16, dyn.capacity)
        self.assertEqual(10, dyn.count)


if __name__ == '__main__':
    unittest.main()
