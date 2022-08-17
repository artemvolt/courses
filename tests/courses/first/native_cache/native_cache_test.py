import unittest
import sys

from courses.first.native_cache.native_cache import NativeCache

sys.path.append('/var/www/courses')

# noinspection PyPep8

class NativeCacheTest(unittest.TestCase):

    def test_hit(self):
        cache = NativeCache(2)
        self.assertEqual([0,0], cache.hits)
        cache.put('hello', 1)
        self.assertEqual([1, 0], cache.hits)
        cache.put('hello', 1)
        self.assertEqual([2, 0], cache.hits)
        cache.put('ehllo', 2)
        self.assertEqual([2, 1], cache.hits)
        cache.get('hello')
        self.assertEqual([3, 1], cache.hits)
        cache.get('ehllo')
        self.assertEqual([3, 2], cache.hits)
        cache.put('helol', 2)
        self.assertEqual([3, 0], cache.hits)
        cache.put('helol', 2)
        cache.put('helol', 2)
        cache.put('helol', 2)
        cache.put('helol', 2)
        self.assertEqual([3, 4], cache.hits)
        cache.put('hlloe', 2)
        self.assertEqual([0, 4], cache.hits)