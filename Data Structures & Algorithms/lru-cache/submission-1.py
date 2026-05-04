class Node:
    def __init__(self,key,val=0,next=None,prev=None):
        self.key = key
        self. val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummy = Node(None)
        self.last = Node(None)
        self.count = 0

        self.dummy.next = self.last
        self.last.prev = self.dummy

    def get(self, key: int) -> int:
        

        if key in self.cache:
            curr = self.cache[key]

            temp_prev = curr.prev
            temp_next = curr.next

            temp_prev.next = temp_next
            temp_next.prev = temp_prev

            curr.next = self.dummy.next
            curr.prev = self.dummy
            self.dummy.next = curr
            curr.next.prev = curr

            test = self.dummy
            print(f"get {key}",end=':')
            while test:
                print(test.key,end=',')
                test = test.next
            print(f":{self.cache.keys()}")

            return self.cache[key].val
            
        else:
            print(f"not found key: {key}")
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            curr = self.cache[key]

            temp_prev = curr.prev
            temp_next = curr.next

            temp_prev.next = temp_next
            temp_next.prev = temp_prev

            curr.next = self.dummy.next
            curr.prev = self.dummy
            self.dummy.next = curr
            curr.next.prev = curr

            self.cache[key].val = value
            print("already in ",end=':')
            
        else:
            new_node = Node(key=key,val = value)
            new_node.next = self.dummy.next
            new_node.prev = self.dummy
            new_node.next.prev = new_node
            self.dummy.next = new_node

            self.cache[key] = new_node
            self.count += 1

            if self.count > self.capacity:
                last_key = self.last.prev.key
                temp_prev = self.last.prev.prev
                temp_prev.next = self.last
                self.last.prev = temp_prev

                del self.cache [last_key]
                self.count -= 1
        print(f"put {key}",end=':')
        test = self.dummy
        while test:
                print(test.key,end=',')
                test = test.next
        print(f":{self.cache.keys()}")



