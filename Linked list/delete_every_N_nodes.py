#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    if M==0:
        return None
    if head==None or N<=0 or M<0:
        return head
    curr=head
    while (curr):
        count1=0
        while count1<M-1 :
            if curr is None:
                return head
            curr=curr.next
            count1=count1+1
        if curr is None:
            return
        prev=curr
        curr=curr.next
        for i in range(0,N):
            if curr==None:
                break
            next=curr.next
            curr=next
        prev.next=curr
    return head    
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
m=int(input())
n=int(input())
l = skipMdeleteN(l, m, n)
printll(l)

