#!/usr/bin/python
"""
   Various types of sorting
"""


def bubble_sort(_list):
    for i in range(len(_list)):
        for j in range(i, len(_list)):
            if _list[i] > _list[j]:
                _list[i], _list[j] = _list[j], _list[i]
    return _list

if __name__ == '__main__':
    import random
    test_list = random.sample(range(-5, 10), 10)
    print "Unsorted:"
    print test_list
    print "Sorted:"
    print bubble_sort(test_list)