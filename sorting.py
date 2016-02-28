#!/usr/bin/python
"""
   Various types of sorting
"""
import random
import timeit

test_list = random.sample(range(-5, 10), 10)


def bubble_sort(_list):
    for i in range(len(_list)):
        for j in range(i, len(_list)):
            if _list[i] > _list[j]:
                _list[i], _list[j] = _list[j], _list[i]
    return _list


def improve_bubble_sort(_list):
    for i in range(len(_list)):
        swaps = 0
        for j in range(i, len(_list)):
            if _list[i] > _list[j]:
                _list[i], _list[j] = _list[j], _list[i]
                swaps += 1
            if swaps == 0:
                break
    return _list


if __name__ == '__main__':
    print "Unsorted:"
    print test_list
    print "Sorted by Bubble sort:"
    print bubble_sort(test_list)
    print "time for basic bubble sort"
    t = timeit.Timer(stmt="sorting.bubble_sort(sorting.test_list)", setup="import sorting")
    print t.timeit(5)
    print "Sorted by Improved Bubble sort:"
    print improve_bubble_sort(test_list)
    print "time for improved bubble sort"
    t = timeit.Timer(stmt="sorting.improve_bubble_sort(sorting.test_list)", setup="import sorting")
    print t.timeit(5)
