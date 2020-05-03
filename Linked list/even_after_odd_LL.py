#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    if head is None or head.next is None:
        return head
    oddH=None
    oddT=None
    evenH=None
    evenT=None
    while head is not None:
        if(head.data%2 != 0):
            if oddH is None:
                oddH=head
                oddT=head
            else:
                oddT.next=head
                oddT=oddT.next
            head=head.next    
        else:
            if evenH is None:
                evenH=head
                evenT=head
            else:
                evenT.next=head
                evenT=evenT.next
            head=head.next  
    if oddH is None:
        oddH=evenH
    elif evenH is None:
        oddT.next=None
    else:
        oddT.next=evenH
        evenT.next=None
    return oddH
    pass

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)

