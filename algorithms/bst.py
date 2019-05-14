#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# Binary Search Tree Implementation

class Tree(object):
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node

    def subtreeSize(self, node):
        return 1 + sum(self.subtreeSize(c) for c in node.getChildren())

    def size(self):
        if (self.root == None):
            return 0
        else:
            return self.subtreeSize(self.root)


class BinaryNode:
    def __init__(self, v):
        self.val = v
        self.leftChild = None
        self.rightChild = None
    def get(self):
        return self.val
    def set(self, v):
        self.val = v
    def getChildren(self):
        children = []
        if self.leftChild != None:
            children.append(self.leftChild)
        if self.rightChild != None:
            children.append(self.rightChild)
        return children

class BinarySearchTree(Tree):
    def insert(self, val):
        if self.root == None:
                self.setRoot(BinaryNode(val))
        else:
            currentRoot = self.root
            while(True):
                if val <= currentRoot.get():
                    if currentRoot.leftChild != None:
                        currentRoot = currentRoot.leftChild
                    else:
                        currentRoot.leftChild = BinaryNode(val)
                        break
                else:
                    if currentRoot.rightChild != None:
                       currentRoot = currentRoot.rightChild
                    else:
                        currentRoot.rightChild = BinaryNode(val)
                        break

    def find(self, val):
        currentRoot = self.root
        while (currentRoot != None and currentRoot.get() != val):
            if val < currentRoot.get():
                currentRoot = currentRoot.leftChild
            else:
                currentRoot = currentRoot.rightChild

        if currentRoot == None:
            return False
        else:
            return True

if __name__ == "__main__":
    btree = BinarySearchTree()
    vals = [5, 3, 9, 4, 1, 7, 30]
    for val in vals:
        btree.insert(val)
    print("Tree size is %i" % int(btree.size()))
    tests = [8, 7, 1, 5]
    for t in tests:
        print("find(%i) = %s" % (t, ("True" if btree.find(t) else "False")))
