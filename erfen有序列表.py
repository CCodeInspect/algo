#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: pauline
Created on 27/05/2021 13:17 PM
"""

"""128 个名字的有序列表，二分查找其中一个名字"""


def get_a_name(list_name, name):
    first_index = 0
    last_index = len(list_name) - 1
    while first_index < last_index:
        mid_index = int((first_index + last_index) / 2)  # mid_index 是下下标
        """需要int转一下，否则报TypeError: list indices must be integers or slices, not float"""
        actual_element = list_name[mid_index]  # actual_element 指的是实际的list的某个元素，而mid_index是list的下标
        if actual_element == name:
            print('找到了')
            return actual_element
        elif actual_element > name:
            last_index = last_index - 1
            print(actual_element)
        else:
            first_index = first_index + 1
            print(actual_element)
            return None


if __name__ == '__main__':
    get_a_name([1, 2, 3, 4, 5, 6, 7], 999)
