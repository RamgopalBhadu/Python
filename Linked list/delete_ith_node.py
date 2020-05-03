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
def delete(head, i):
    len=length(head)
    if i<0 or i>=len:
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count=count+1
    if count>=1:  
        if i<len:
            prev.next=curr.next
        else:
            return
    else:
        return 
    return head
    # A linked list and a position i, delete the node of ith position from
    # Linked List iteratively. If position i is greater than length of LL, then
    # you should return the same LL without any change. Indexing starts from 0.
    # You don't need to print the elements, just delete the node and return the
    # head of updated LL.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
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
l = delete(l, i)
printll(l)

