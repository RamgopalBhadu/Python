#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1,head2):
    finalhead=None
    tail=None
    if (head1.data<=head2.data):
        finalhead=head1
        tail=head1
        head1=head1.next
    else:
        finalhead=head2
        tail=head2
        head2=head2.next
    while(head1 is not None and head2 is not None):
        if(head1.data<=head2.data):
            tail.next=head1
            tail=tail.next
            head1=head1.next
        else:
            tail.next=head2
            tail=tail.next
            head2=head2.next
    while(head1 is not None):
        tail.next=head1
        tail=tail.next
        head1=head1.next
    while(head2 is not None):
        tail.next=head2
        tail=tail.next
        head2=head2.next        
    tail.next=None
    return finalhead        
    pass
    # two linked lists sorted in increasing order. Merge them in such
    # a way that the result list is also sorted (in increasing order). Try
    # solving with O(1) auxiliary space (in-place). You just need to return the
    # head of new linked list, don't print the elements.

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
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)

