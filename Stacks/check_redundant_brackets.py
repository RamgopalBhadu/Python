#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def checkRedundant(str):
#### Implement Your Code Here
    # create a stack of characters  
    st = []  
  
    # Iterate through the given expression  
    for ch in str:  
  
        # if current character is close  
        # parenthesis ')'  
        if (ch == ')'):  
            top = st[-1]  
            st.pop()  
  
            # If immediate pop have open parenthesis  
            # '(' duplicate brackets found  
            flag = True
  
            while (top != '('):  
  
                # Check for operators in expression  
                if (top == '+' or top == '-' or
                    top == '*' or top == '/'):  
                    flag = False
  
                # Fetch top element of stack  
                top = st[-1]  
                st.pop() 
  
            # If operators not found  
            if (flag == True): 
                return True
  
        else: 
            st.append(ch) # append open parenthesis '(',  
                          # operators and operands to stack 
    return False

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')




