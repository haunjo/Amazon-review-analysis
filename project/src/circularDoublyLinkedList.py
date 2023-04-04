from list.bidirectNode import BidirectNode
import pandas as pd

class CircularDoublyLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item


class CircularDoublyLinkedListFilter:
    def __init__(self, dataset):
        self.list = [dataset.getNode(0).item.keys()]
        self.find(dataset)
    def find(self, dataset):
        for i in dataset:
            if int(i['star_rating']) > 4 and 2 < int(i['review_date'][5:7]) < 7 and i['verified_purchase'] == 'Y':
                self.list.append(i.values())
            



class CircularDoublyLinkedList:
    dummy = [None]*15
    
    def __init__(self):
        self.__head = BidirectNode(CircularDoublyLinkedList.dummy, None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
        
    def insert(self, i:int, newItem):
        if (i >= 0 and i <= self.__numItems):
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
            
    def append(self, newItem):
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1
        
    def pop(self, *args):
    # 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만족
        if self.isEmpty():
            return None
# 인덱스 고 결정
        if len(args) != 0: # pop(k)과 같이 인자가 있으면 1 = K 할당
            i = args[0]
        if len(args) == 0 or i== -1:# pop()에 인자가 없거나 pop (-1)이면 1에 맨 끝 인덱스 할당
            i = self.__numItems - 1
# 1번 원소 삭제
        if (i >= 0 and i <= self.__numItems - 1):
            curr = self.getNode(i)
            retItem = curr.item
            curr.prev.next = curr. next
            curr.next.prev = curr. prev
            self.__numItems -= 1 
            return retItem
        else:
            return None
        
    def remove(self, x):
        curr = self.findNode(x)
        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr. prev
            self.__numItems -= 1 
            return x
        else:
            return None
        
    def get (self, *args):
    # 가변 파라미터. 인자가 없거나 -10면 마지막 원소로 처리하>
        if self.isEmpty(): return None
# 인덱스 1 결정
        if len(args) != 0:
# pop(k)과 같이 인자가 있으면
            i = args [0]
        if len(args) == 0 or i == -1:
# pop()에 인자가
            i = self.__numItems - 1
# 1번 원소 리턴
        if (i >= 0 and i <= self.__numItems - 1):
                return self.getNode (i).item   
        else:
            return None
        
    def index(self, x):
        cnt = 0
        for element in self:
            if element == x:
                return cnt 
            cnt += 1
        return -12345
    
    def isEmpty(self):
        return self.__numItems == 0
    
    def size(self):
        return self.__numItems
    
    def clear(self):
        self.__head == BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
    def count(self, x):
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt

    def extend(self, a):
        for element in a:
            self.append(element)
            
    def copy(self):
        a = CircularDoublyLinkedList()
        for element in self:
            a.append(element)
        return a
    
    def reverse(self):
        prev = self.__head; curr = prev.next; next = curr.next
        self.__head.next = prev.prev; self.__head.prev = curr
        for i in range(self.__numItems):
            curr.next = prev; curr.prev = next
            prev = curr; curr = next; next = next.next
    
    def sort(self):
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)
    
            
    def __findNode(self,x):
        curr = self.__head.next
        while curr != self.__head:
            if curr.item == x:
                return curr
            else:
                curr = curr.next
        return None
    
    def getNode(self, i:int):
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr
    
    def printList(self):
        for element in self:
            print(element, end=' ')
        print()
        
    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)
    
    def filter(self, data : CircularDoublyLinkedListFilter):
        df = pd.DataFrame(data.list[1:], columns=data.list[0])
        df = df.sort_values(by="product_title", key= lambda x : df.value_counts('product_title')[x], ascending= False)        
        return df[:][['product_title', 'review_id', 'star_rating', 'helpful_votes', 'review_date']]
        
