# AI2_2017


```


String1



donuts
 OK  got: 'Number of donuts: 4' expected: 'Number of donuts: 4'
 OK  got: 'Number of donuts: 9' expected: 'Number of donuts: 9'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
both_ends
 OK  got: 'spng' expected: 'spng'
 OK  got: 'Helo' expected: 'Helo'
 OK  got: '' expected: ''
 OK  got: 'xyyz' expected: 'xyyz'
fix_start
 OK  got: 'ba**le' expected: 'ba**le'
 OK  got: 'a*rdv*rk' expected: 'a*rdv*rk'
 OK  got: 'goo*le' expected: 'goo*le'
 OK  got: 'donut' expected: 'donut'
mix_up
 OK  got: 'pox mid' expected: 'pox mid'
 OK  got: 'dig donner' expected: 'dig donner'
 OK  got: 'spash gnort' expected: 'spash gnort'
 OK  got: 'fizzy perm' expected: 'fizzy perm'
 
 
 
 string2
 
 
 
 verbing
 OK  got: 'hailing' expected: 'hailing'
 OK  got: 'swimingly' expected: 'swimingly'
 OK  got: 'do' expected: 'do'
not_bad
 OK  got: 'This movie is good' expected: 'This movie is good'
 OK  got: 'This dinner is good!' expected: 'This dinner is good!'
 OK  got: 'This tea is not hot' expected: 'This tea is not hot'
 OK  got: "It's bad yet not" expected: "It's bad yet not"
front_back
 OK  got: 'abxcdy' expected: 'abxcdy'
 OK  got: 'abcxydez' expected: 'abcxydez'
 OK  got: 'KitDontenut' expected: 'KitDontenut'
 
 
 
 list1
 
 
 
 match_ends
 OK  got: 3 expected: 3
 OK  got: 2 expected: 2
 OK  got: 1 expected: 1
front_x
 OK  got: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
 OK  got: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
 OK  got: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
sort_last
 OK  got: [(2, 1), (3, 2), (1, 3)] expected: [(2, 1), (3, 2), (1, 3)]
 OK  got: [(3, 1), (1, 2), (2, 3)] expected: [(3, 1), (1, 2), (2, 3)]
 OK  got: [(2, 2), (1, 3), (3, 4, 5), (1, 7)] expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
 
 
 
 
 list2
 
 
 remove_adjacent
 OK  got: [1, 2, 3] expected: [1, 2, 3]
 OK  got: [2, 3] expected: [2, 3]
 OK  got: [] expected: []
linear_merge
  X  got: ['zz', 'xx', 'aa', 'bb', 'cc'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
  X  got: ['xx', 'aa', 'bb', 'cc', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
  X  got: ['bb', 'bb', 'aa', 'aa', 'aa'] expected: ['aa', 'aa', 'aa', 'bb', 'bb']
```

lab2

Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:/Users/student.INFORMATYKA/Desktop/lab2.py ===========
>>> hellow()
Hello, World!
>>> ox()
  |  |  
--------
  |  |  
--------
  |  |  
>>> XLox()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    XLox()
NameError: name 'XLox' is not defined
>>> XLxo()
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
========+========+========
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
========+========+========
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
>>> buzz(41)
408
>>> collatz(13)
10
>>> 
>>> convert(212)
100.0
>>> ob_ref()
[1, 0, 0]
['a', '', '']
[[1], [1], [1]]
>>> gcd(10, 25)
5
>>> flip_dict({"CA" : "US", "NY": "US", "ON": "CA"})
{'US': ['CA', 'NY'], 'CA': ['ON']}
>>> comprehension_read()
[1, 2, 3, 4]
[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
[0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9]
['python']
[None, None, None]
[[3, 2, 1, 12], ['a', 'b', 'c', 'aaaa'], [('do',), ['re'], 'mi', ('do', 'do', 'do', 'do')]]
['Y', 'O', 'N']
{8, 2, 3, 5}
>>> comprehension_write()
[1, 3, 5, 7]
[True, False, True, False]
['sam', 'guido']
['A', 'O', 'P']
['apple', 'pear']
[('apple', 5), ('orange', 6), ('pear', 4)]
{'pear': 4, 'orange': 6, 'apple': 5}
>>> 
