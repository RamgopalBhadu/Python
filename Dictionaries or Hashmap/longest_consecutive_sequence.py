#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def longestConsecutiveIncreasingSequence(l):
    d = dict()
    b = [l[0]]
    for i in l:
        d[i] = d.get(i, True)
    for i in l:
        if d[i] == True:
            d[i] = False
            j = i
            len1 = 1
            start1 = j
            a = [j]

            while d.get(j - 1) != None:
                len1 += 1
                a.append(j-1)
                d[j-1] = False
                start1 = j - 1
                j -= 1
            j = i


            while d.get(j + 1) != None:
                len1 += 1
                a.append(j+1)
                d[j+1] = False
                j += 1
            if len(a) > len(b):
                b = a
            elif len(a) == len(b):
                min_a = min(a)
                min_b = min(b)
                if l.index(min_a) < l.index(min_b):
                    b = a

    
    for i in b:
        print(i)


n = int(input())
l = list(int(i) for i in input().strip().split(' '))
longestConsecutiveIncreasingSequence(l)

