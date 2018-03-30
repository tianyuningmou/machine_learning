# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: middle_noun.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/30 下午2:36

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/30 下午2:36
"""

# 不排序寻找中位数（数据中中位数不能出现多次，后面解决）
def find_middle_noun(num_list):
    min_list = list()
    max_list = list()
    result = list()
    if len(num_list) % 2 == 0:
        for i in range(len(num_list)):
            for j in range(len(num_list)):
                if num_list[i] < num_list[j]:
                    min_list.append(num_list[j])
                if num_list[i] > num_list[j]:
                    max_list.append(num_list[j])
            if abs(len(min_list) - len(max_list)) != 1:
                min_list = []
                max_list = []
            else:
                result.append(num_list[i])
                min_list = []
                max_list = []
    else:
        for i in range(len(num_list)):
            for j in range(len(num_list)):
                if num_list[i] < num_list[j]:
                    min_list.append(num_list[j])
                if num_list[i] > num_list[j]:
                    max_list.append(num_list[j])
            if len(min_list) != len(max_list):
                min_list = []
                max_list = []
            else:
                result.append(num_list[i])
    return result


if __name__ == '__main__':
    result = find_middle_noun([1, 2, 3, 4, 5, 6])
    print(result[0] if len(result) == 1 else (result[0] + result[1]) / 2)
