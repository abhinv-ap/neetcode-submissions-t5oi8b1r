class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.next,self.prev=None,None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.n=0
        self.cache={}
        self.lru=Node(0,0)
        self.mru=Node(0,0)
        self.lru.next=self.mru
        self.mru.prev=self.lru

    def rm(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        node.next=self.mru
        node.prev=self.mru.prev
        self.mru.prev.next=node
        self.mru.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.rm(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val=value
            self.rm(self.cache[key])
            self.insert(self.cache[key])
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.insert(node)
            self.n+=1
        if self.n>self.cap:
            del self.cache[self.lru.next.key]
            self.rm(self.lru.next)
            self.n-=1
        


    