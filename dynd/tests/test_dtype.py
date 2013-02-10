import sys
import unittest
from dynd import nd, ndt

class TestDType(unittest.TestCase):

    def test_bool_dtype_properties(self):
        self.assertEqual(type(ndt.bool), nd.dtype)
        self.assertEqual(str(ndt.bool), 'bool')
        self.assertEqual(ndt.bool.element_size, 1)
        self.assertEqual(ndt.bool.alignment, 1)

    def test_int_dtype_properties(self):
        self.assertEqual(type(ndt.int8), nd.dtype)
        self.assertEqual(str(ndt.int8), 'int8')
        self.assertEqual(ndt.int8.element_size, 1)
        self.assertEqual(ndt.int8.alignment, 1)

        self.assertEqual(type(ndt.int16), nd.dtype)
        self.assertEqual(str(ndt.int16), 'int16')
        self.assertEqual(ndt.int16.element_size, 2)
        self.assertEqual(ndt.int16.alignment, 2)

        self.assertEqual(type(ndt.int32), nd.dtype)
        self.assertEqual(str(ndt.int32), 'int32')
        self.assertEqual(ndt.int32.element_size, 4)
        self.assertEqual(ndt.int32.alignment, 4)

        self.assertEqual(type(ndt.int64), nd.dtype)
        self.assertEqual(str(ndt.int64), 'int64')
        self.assertEqual(ndt.int64.element_size, 8)
        self.assertEqual(ndt.int64.alignment, 8)

    def test_uint_dtype_properties(self):
        self.assertEqual(type(ndt.uint8), nd.dtype)
        self.assertEqual(str(ndt.uint8), 'uint8')
        self.assertEqual(ndt.uint8.element_size, 1)
        self.assertEqual(ndt.uint8.alignment, 1)

        self.assertEqual(type(ndt.uint16), nd.dtype)
        self.assertEqual(str(ndt.uint16), 'uint16')
        self.assertEqual(ndt.uint16.element_size, 2)
        self.assertEqual(ndt.uint16.alignment, 2)

        self.assertEqual(type(ndt.uint32), nd.dtype)
        self.assertEqual(str(ndt.uint32), 'uint32')
        self.assertEqual(ndt.uint32.element_size, 4)
        self.assertEqual(ndt.uint32.alignment, 4)

        self.assertEqual(type(ndt.uint64), nd.dtype)
        self.assertEqual(str(ndt.uint64), 'uint64')
        self.assertEqual(ndt.uint64.element_size, 8)
        self.assertEqual(ndt.uint64.alignment, 8)

    def test_float_dtype_properties(self):
        self.assertEqual(type(ndt.float32), nd.dtype)
        self.assertEqual(str(ndt.float32), 'float32')
        self.assertEqual(ndt.float32.element_size, 4)
        self.assertEqual(ndt.float32.alignment, 4)

        self.assertEqual(type(ndt.float64), nd.dtype)
        self.assertEqual(str(ndt.float64), 'float64')
        self.assertEqual(ndt.float64.element_size, 8)
        self.assertEqual(ndt.float64.alignment, 8)

    def test_complex_dtype_properties(self):
        self.assertEqual(type(ndt.cfloat32), nd.dtype)
        self.assertEqual(str(ndt.cfloat32), 'complex<float32>')
        self.assertEqual(ndt.cfloat32.element_size, 8)
        self.assertEqual(ndt.cfloat32.alignment, 4)

        self.assertEqual(type(ndt.cfloat64), nd.dtype)
        self.assertEqual(str(ndt.cfloat64), 'complex<float64>')
        self.assertEqual(ndt.cfloat64.element_size, 16)
        self.assertEqual(ndt.cfloat64.alignment, 8)

    def test_fixedstring_dtype_properties(self):
        d = ndt.make_fixedstring_dtype('ascii', 10)
        self.assertEqual(str(d), 'fixedstring<ascii,10>')
        self.assertEqual(d.element_size, 10)
        self.assertEqual(d.alignment, 1)
        self.assertEqual(d.encoding, 'ascii')

        d = ndt.make_fixedstring_dtype('ucs_2', 10)
        self.assertEqual(str(d), 'fixedstring<ucs_2,10>')
        self.assertEqual(d.element_size, 20)
        self.assertEqual(d.alignment, 2)
        self.assertEqual(d.encoding, 'ucs_2')

        d = ndt.make_fixedstring_dtype('utf_8', 10)
        self.assertEqual(str(d), 'fixedstring<utf_8,10>')
        self.assertEqual(d.element_size, 10)
        self.assertEqual(d.alignment, 1)
        self.assertEqual(d.encoding, 'utf_8')

        d = ndt.make_fixedstring_dtype('utf_16', 10)
        self.assertEqual(str(d), 'fixedstring<utf_16,10>')
        self.assertEqual(d.element_size, 20)
        self.assertEqual(d.alignment, 2)
        self.assertEqual(d.encoding, 'utf_16')

        d = ndt.make_fixedstring_dtype('utf_32', 10)
        self.assertEqual(str(d), 'fixedstring<utf_32,10>')
        self.assertEqual(d.element_size, 40)
        self.assertEqual(d.alignment, 4)
        self.assertEqual(d.encoding, 'utf_32')

    def test_scalar_dtypes(self):
        self.assertEqual(ndt.bool, nd.dtype(bool))
        self.assertEqual(ndt.int32, nd.dtype(int))
        self.assertEqual(ndt.float64, nd.dtype(float))
        self.assertEqual(ndt.cfloat64, nd.dtype(complex))

    def test_fixedbytes_dtype(self):
        d = ndt.make_fixedbytes_dtype(4, 4)
        self.assertEqual(str(d), 'fixedbytes<4,4>')
        self.assertEqual(d.element_size, 4)
        self.assertEqual(d.alignment, 4)

        d = ndt.make_fixedbytes_dtype(9, 1)
        self.assertEqual(str(d), 'fixedbytes<9,1>')
        self.assertEqual(d.element_size, 9)
        self.assertEqual(d.alignment, 1)

        # Alignment must not be greater than element_size
        self.assertRaises(RuntimeError, ndt.make_fixedbytes_dtype, 1, 2)
        # Alignment must be a power of 2
        self.assertRaises(RuntimeError, ndt.make_fixedbytes_dtype, 6, 3)
        # Alignment must divide into the element_size
        self.assertRaises(RuntimeError, ndt.make_fixedbytes_dtype, 6, 4)

if __name__ == '__main__':
    unittest.main()