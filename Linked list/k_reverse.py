#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kReverse(head, k) :
    prev = None
    curr = head  
    temp = None
    tail = None
    newHead = None
    join = None
    t = 0
    while (curr) :  
        t = k  
        join = curr  
        prev = None
        while (curr and t > 0):
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 
            t = t - 1
        if (newHead == None):  
            newHead = prev
        if (tail != None):  
            tail.next = prev 
        tail = join
    return newHead
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
l = kReverse(l, i)
printll(l)

