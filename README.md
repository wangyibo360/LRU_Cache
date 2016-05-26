# LRU_Cache
LRU cache with conditional updating

Examples
--------

### Example 1

Use default node on LRU cache.
The cache will update node by least recently used naturally.
```
from lru import LRU_Cache
from lru import Node

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

```

The output should be:
```
{ value: 1, key: a, } <--> None
{ value: 2, key: b, } <--> { value: 1, key: a, } <--> None
{ value: 3, key: a, } <--> { value: 2, key: b, } <--> None
```

### Example 2

Use client defined node on LRU cache.
You can control updating behavior by defining the function "__lt__"
```
class ClientNode(Node):

    def __init__(self, key, value, timestamp):
        super(ClientNode, self).__init__(key, value)
        self.timestamp = timestamp

    def __str__(self):
        return '(%s : %s : %s)' % (self.key, self.value, self.timestamp)

    def __lt__(self, other):
        return self.timestamp < other.timestamp


lru_client = LRU_Cache(5)
now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
node = ClientNode('a', 1, now)
lru_client.set(node)
print lru_client

now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
node = ClientNode('b', 2, now)
lru_client.set(node)
print lru_client

now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
node = ClientNode('a', 3, now)
lru_client.set(node)
print lru_client

now = datetime.datetime.now()
now = now - datetime.timedelta(hours=1)
now = now.strftime('%Y-%m-%d %H:%M:%S')
node = ClientNode('b', 4, now)
lru_client.set(node)
print lru_client
```

The output should be:
```
{ timestamp: 2016-05-26 11:43:56, value: 1, key: a, } <--> None
{ timestamp: 2016-05-26 11:43:57, value: 2, key: b, } <--> { timestamp: 2016-05-26 11:43:56, value: 1, key: a, } <--> None
{ timestamp: 2016-05-26 11:43:58, value: 3, key: a, } <--> { timestamp: 2016-05-26 11:43:57, value: 2, key: b, } <--> None
{ timestamp: 2016-05-26 11:43:58, value: 3, key: a, } <--> { timestamp: 2016-05-26 11:43:57, value: 2, key: b, } <--> None
```
