#!/usr/bin/python
# encoding: utf-8

from __future__ import print_function

import sys
import json

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return '(%s : %s)' % (self.key, self.value)

    __repr__ = __str__


class TwoWayLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __str__(self):
        output = ''
        p = self.head
        while p:
            output += '{ '
            for k,v in p.__dict__.iteritems():
                if k == 'prev' or k == 'next':
                    continue
                output += '%s: %s, ' % (k, v)
            output += '} <--> '
            p = p.next
        output += '%s' % None
        return output

    __repr__ = __str__

    def isEmpty(self):
        return self._length == 0

    @property
    def length(self):
        return self._length

    def insert_head(self, node):
        head = self.head
        self._length += 1
        if head:
            node.next = head
            head.prev = node
            self.head = node
            node.prev = None
        else:
            self.head = self.tail = node
            node.prev = node.next = None
            return

    def append(self, node):
        tail = self.tail
        self._length += 1
        if tail:
            node.prev = tail
            tail.next = node
            self.tail = node
            node.next = None
        else:
            self.head = self.tail = node
            node.prev = node.next = None

    def insert(self, index, node):
        if index < 0 or index > self.length:
            raise IndexError('Index should be in range of [%s - %s], but your give %s' % (0, max(self._length-1, 0), index))
        if self.isEmpty() or index == 0:
            self.insert_head(node)
            return
        if index == self.length:
            self.append(node)
            return
        self._length += 1
        i = 1
        prev = self.head
        while i < index:
            prev = prev.next
            i += 1
        next = prev.next
        node.next = next
        prev.next = node
        node.prev = prev
        if next:
            next.prev = node


    def delete_head(self):
        head = self.head
        if head:
            self._length -= 1
            next = head.next
            self.head = next
            head.next = None
            if next:
                next.prev = None
            else:
                self.tail = None
            return head
        else:
            return None


    def pop(self):
      tail = self.tail
      if tail:
          self._length -= 1
          prev = tail.prev
          self.tail = prev
          tail.prev = None
          if prev:
              prev.next = None
          else:
              self.head = None
          return tail
      else:
          return None

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index should be in range of [%s - %s], but your give %s' % (0, max(self._length-1, 0), index))
        if index == 0:
            return self.delete_head()
        if index == self.length - 1:
            return self.pop()
        self._length -= 1
        i = 0
        p = self.head
        while i < index:
            p = p.next
            i += 1
        prev = p.prev
        next = p.next
        prev.next = next
        p.prev = None
        p.next = None
        if next:
            next.prev = prev
        return p

    def remove_node(self, node):
        if not node:
            return
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            next = node.next
            self.head = next
            next.prev = None
            node.next = None
            return
        elif node == self.tail:
            prev = node.prev
            self.tail = prev
            prev.next = None
            node.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev


    def reverse(self):
        output = ''
        p = self.tail
        while p:
            output += '(%s : %s) <--> ' % (p.key, p.value)
            p = p.prev
        output += '%s' % None
        print(output)


class LRU_Cache_Iterator(object):

    def __init__(self, cache):
        self.linklist = cache.linklist
        self.index = self.linklist.head

    def __iter__(self):
        return self

    def next(self):
        if not self.index:
            raise StopIteration
        else:
            node = self.index
            self.index = self.index.next
            return node


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = {}
        self.linklist = TwoWayLinkedList()

    def __iter__(self):
        return LRU_Cache_Iterator(self)

    def get(self, node):
        key = node.key
        if key in self.table:
            node = self.table[key]
            self.linklist.remove_node(node)
            self.linklist.insert_head(node)
            return node
        else:
            return None

    def set(self, node):
        key = node.key
        if key in self.table:
            _node = self.table[key]
            update = True
            if hasattr(node, '__lt__'):
                update = _node < node
            if update:
                self.table[key] = node
                self.linklist.remove_node(_node)
                self.linklist.insert_head(node)
        else:
            if self.size == self.capacity:
                _node = self.linklist.pop()
                del self.table[_node.key]
                self.size -= 1
            self.table[key] = node
            self.linklist.insert_head(node)
            self.size += 1


    def __str__(self):
        output = ''
        head = self.linklist.head
        p = head
        while p:
            output += '{ '
            for k,v in p.__dict__.iteritems():
                if k == 'prev' or k == 'next':
                    continue
                output += '%s: %s, ' % (k, v)
            output += '} <--> '
            p = p.next
        output += '%s' % None
        return output

    __repr__ = __str__












