#!/usr/bin/python
# encoding: utf-8

from lru import LRU_Cache
from lru import Node

import datetime
import time


class ClientNode(Node):

    def __init__(self, key, value, timestamp):
        super(ClientNode, self).__init__(key, value)
        self.timestamp = timestamp

    def __str__(self):
        return '(%s : %s : %s)' % (self.key, self.value, self.timestamp)

    def __lt__(self, other):
        return self.timestamp < other.timestamp


def main():
    lru = LRU_Cache(5)
    node = Node('a', 1)
    lru.set(node)
    print lru

    node = Node('b', 2)
    lru.set(node)
    print lru

    node = Node('a', 3)
    lru.set(node)
    print lru
    print '\n'

    print 'LRU with client node'
    lru_client = LRU_Cache(5)
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    node = ClientNode('a', 1, now)
    lru_client.set(node)
    print lru_client
    time.sleep(1)

    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    node = ClientNode('b', 2, now)
    lru_client.set(node)
    print lru_client
    time.sleep(1)

    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    node = ClientNode('a', 3, now)
    lru_client.set(node)
    print lru_client
    time.sleep(1)

    now = datetime.datetime.now()
    now = now - datetime.timedelta(hours=1)
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    node = ClientNode('b', 4, now)
    lru_client.set(node)
    print lru_client
    time.sleep(1)


if __name__ == "__main__":
    main()
