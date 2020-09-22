class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None:
       return llist_2
    elif llist_2.head is None:
       return llist_1
    out=LinkedList()
    dic1= {}
    node1=llist_1.head
    ## save all unique nodes into hashmap 1
    while node1:
        if node1.value not in dic1:
            out.append(node1.value)
            dic1[node1.value]= 1
        node1=node1.next
    node2=llist_2.head
    dic2={}
    while node2:
        dic2[node2.value]= 2
        if node2.value not in dic1 and node2.value not in dic2:
            out.append(node2.value)
        node2=node2.next
    return out
    


def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None or llist_2.head is None:
        return LinkedList()
    dic1= {}
    node1=llist_1.head
    while node1:
        if node1.value not in dic1:
            dic1[node1.value]= 1
        node1=node1.next
    out=LinkedList()
    node2=llist_2.head
    dic2={}
    while node2:
        if node2.value in dic1 and node2.value not in dic2:
            out.append(node2.value)
            dic2[node2.value]= 2
        node2=node2.next
    return out


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3 both lists are empty

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))


# Test case 4 very large number
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [i for i in range(10000)]
element_2 = [(i+2) * 2 for i in range(9999)]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))