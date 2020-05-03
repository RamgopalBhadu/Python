#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midpoint_linkedlist(head):
    if head is None:
        return None
    slow=head
    fast=head
    while fast.next is not None and fast.next.next is not None :
        slow=slow.next
        fast=fast.next.next
    return slow         
def print_linkedlist_spl(head):
    curr=head
    prev=None
    while(curr is not None):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
def check_palindrome(head) :
    mid=midpoint_linkedlist(head)
    h2=mid.next
    mid.next=None
    head2=print_linkedlist_spl(h2)

    while head is not None and head2 is not None:
        if(head.data!=head2.data):
            return 'false'
        head=head.next
        head2=head2.next
    return 'true'   
        
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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
print(ans)

