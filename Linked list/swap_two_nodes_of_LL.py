#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head, i, j):
   #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    counti=0
    countj=0
    curr = head
    prev=None
    if(i<j):
        I=i
        J=j
    else:
        I=j
        J=i
    #iprev=None
    #jprev=None
    #ihead=None
    #jhead=None
    #iheadnext=None
    #jheadnext=None
    while curr is not None:
        if counti>I and countj>J:
            break
        if counti == I:
            ihead=curr
            if(curr.next is not None):
                iheadnext=curr.next
            else:
                iheadnext=None
            iprev=prev
           
        if countj==J:
            jhead = curr
            if(jhead.next is not None):
                jheadnext=jhead.next
            else:
                jheadnext=None
            jprev=prev
        counti+=1
        countj+=1
        prev=curr
        curr=curr.next
    if ihead==jprev:
        if iprev is not None:
            iprev.next=jhead
            jhead.next=ihead
            ihead.next=jheadnext
            return head
        else:
           
            jhead.next=ihead
            ihead.next=jheadnext
            return jhead
    if iprev is None:
        jprev.next=ihead
        jhead.next=iheadnext
        ihead.next=jheadnext
        return jhead
   
       
   
    iprev.next=jhead
    jprev.next=ihead
   
    jhead.next=iheadnext
    ihead.next=jheadnext
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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)

