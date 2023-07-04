class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    # create new Node
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        # make a new node
        new_node = Node(value)

        # if no nodes exist - head & tail will both point to this first node
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        # else make the first node point to this new node, and add it as the end of the linked list by setting tail to it
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
            
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
            
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        curr_index = 0
        temp = self.head
        while curr_index < index:
            temp = temp.next
            curr_index += 1
        return temp
    

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        # we're calling index - 1 since we want the pointer before the new position, not the one after
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        previous = self.get(index-1)
        temp = previous.next
        previous.next = temp.next
        temp.next = None
        self.length -= 1

        return temp
    

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after





# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)

# my_linked_list.reverse()
# print(my_linked_list.print_list())


s = ['h', 'e', 'l','l','o']
x = [i for i in s]
print(x)