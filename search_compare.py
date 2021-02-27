#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import random
import time


# In[29]:


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


# In[36]:


def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found


# In[37]:


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
                
    return found


# In[38]:


def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
    


# In[39]:


def binary_search_recursive (a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


# In[41]:


if __name__ == "__main__":
    """Main entry point"""
   
    import random
    import time
    
    

    random.seed(100)
    
    list_sizes = [500, 1000, 5000]
    
    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            list_sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            start_sort = time.time()
            ordered_list = sequential_search(my_list,random.randint(0, len(my_list) + 100) )
            end_sort = time.time()
            sort_duration = end_sort - start_sort
            total_time += sort_duration
        avg_time = total_time / 100
        print(f"Average time to search list of {list_size} using Sequential search was {avg_time:0.8f} seconds.")
        
        
    for list_size in list_sizes:
        for i in range(100):
            list_sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            start_sort = time.time()
            ordered_list = ordered_sequential_search(my_list, random.randint(0, len(my_list) + 100))
            end_sort = time.time()
            sort_duration = end_sort - start_sort
            total_time += sort_duration
        avg_time = total_time / 100
        print(f"Average time to search list of {list_size} using Ordered sequential search was {avg_time:0.8f} seconds.")  
    
    for list_size in list_sizes:
        for i in range(100):
            list_sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            start_sort = time.time()
            ordered_list = binary_search_iterative(my_list, random.randint(0, len(my_list) + 100))
            end_sort = time.time()
            sort_duration = end_sort - start_sort
            total_time += sort_duration
        avg_time = total_time / 100
        print(f"Average time to search list of {list_size} using binary search iterative  search was {avg_time:0.8f} seconds.")
        
    for list_size in list_sizes:
        for i in range(100):
            list_sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            start_sort = time.time()
            ordered_list = binary_search_recursive(my_list, random.randint(0, len(my_list) + 100))
            end_sort = time.time()
            sort_duration = end_sort - start_sort
            total_time += sort_duration
        avg_time = total_time / 100
        print(f"Average time to search list of {list_size} using binary search recursive was {avg_time:0.8f} seconds.")     


# In[ ]:





# In[ ]:




