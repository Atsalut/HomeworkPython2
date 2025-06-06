import array
import numpy as np
import sys
#Типы данных Python
# x = 1
# print(type(x))
# print(sys.getsizeof(x))
#
# x = 'hello'
# print(type(x))
#
# x = True
# print(type(x))

# l1 = list([])
# print(sys.getsizeof(l1))
#
# l2 = list([1, 2, 3])
# print(sys.getsizeof(l2))
#
# l3 = list([1, '2', True])
# print(l3)

# a1 = array.array('i', [1, 2, 3])
# print(sys.getsizeof(a1))
# print(type(a1))

# 1. Какие еще типы кодов существуют?
#  'b': signed char, 'B': unsigned char, 'u': Unicode character
#  'h': signed short, 'H': unsigned short
#  'i': signed int, 'I': unsigned int
#  'l': signed long, 'L': unsigned long
#  'q': signed long long, 'Q': unsigned long long
#  'f': float, 'd': double

# 2. Напишите код, подобный приведенному выше, но с другим типом

# a2 = array.array('f', [1.23, 2.34, 3.45])
# print(sys.getsizeof(a2))
# print(type(a2))

a = np.array([1, 2, 3, 4, 5])
print (type(a), a)
