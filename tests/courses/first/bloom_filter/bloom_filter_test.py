import unittest

from courses.first.bloom_filter.bloom_filter import BloomFilter


class bloom_filter_test(unittest.TestCase):

    def test_hash_one(self):
        bloom = BloomFilter(32)
        bloom.add('0123456789')
        #self.assertEqual(13, bloom.hash1('0123456789'))
        # self.assertEqual(29, bloom.hash1('1234567890'))
        #self.assertEqual(13, bloom.hash1('8901234567'))
        # self.assertEqual(29, bloom.hash1('9012345678'))

    # def test_hash_two(self):
    #     bloom = BloomFilter(32)
    #     self.assertEqual(5, bloom.hash2('0123456789'))
    #     self.assertEqual(27, bloom.hash2('1234567890'))
    #     self.assertEqual(5, bloom.hash2('8901234567'))
    #     self.assertEqual(27, bloom.hash2('9012345678'))


