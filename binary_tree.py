# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: binary_tree.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/30 上午9:34

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/30 上午9:34
"""


# 二叉树的各种遍历
class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 深度优先
def depth(tree):
    if tree is None:
        return 0
    left, right = depth(tree.left), depth(tree.right)
    return max(left, right) + 1


# 前序遍历
def pre_order(tree):
    if tree is None:
        return
    print(tree.data, end=' ')
    pre_order(tree.left)
    pre_order(tree.right)


# 中序遍历
def mid_order(tree):
    if tree is None:
        return
    mid_order(tree.left)
    print(tree.data, end=' ')
    mid_order(tree.right)


# 后序遍历
def post_order(tree):
    if tree is None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data, end=' ')


# 层次遍历
def level_order(tree):
    if tree is None:
        return
    q = list()
    q.append(tree)
    while q:
        current = q.pop(0)
        print(current.data, end=' ')
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)


# 按层次打印
def level_print(tree):
    if tree is None:
        return
    q = list()
    q.append(tree)
    results = {}
    level = 0
    current_level_num = 1
    nextlevelnum = 0
    d = []
    while q:
        current = q.pop(0)
        current_level_num -= 1
        d.append(current.data)
        if current.left is not None:
            q.append(current.left)
            nextlevelnum += 1
        if current.right is not None:
            q.append(current.right)
            nextlevelnum += 1
        if current_level_num == 0:
            current_level_num = nextlevelnum
            nextlevelnum = 0
            results[level] = d
            d = []
            level += 1
    print(results)


if __name__ == '__main__':
    tree = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    print('前序遍历：', end=' ')
    pre_order(tree)
    print('\n')
    print('中序遍历：', end=' ')
    mid_order(tree)
    print('\n')
    print('后序遍历：', end=' ')
    post_order(tree)
    print('\n')
    print('层次遍历：', end=' ')
    level_print(tree)
