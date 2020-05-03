#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count          
def append_LinkedList(head,n) :
    len=length(head)
    count=0
    curr=head
    while count<len-n-1:
        curr=curr.next
        count=count+1
    h2=curr.next
    curr.next=None
    tail=h2
    while tail.next is not None:
        tail=tail.next
    tail.next=head
    return h2
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
i=int(input())
l = append_LinkedList(l, i)
printll(l)

