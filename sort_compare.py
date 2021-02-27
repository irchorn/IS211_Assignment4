#!/usr/bin/env python
# coding: utf-8

# In[44]:


import random
import time


# In[49]:


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
   


# In[ ]:


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            
        a_list[position] = current_value
        
print("After increments of size", sublist_count, "The list is",a_list)


# In[55]:


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        
        
        sublist_count = sublist_count // 2
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i] 
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap] 
            position = position - gap
        a_list[position] = current_value


# In[56]:


def python_sort(a_list):
    return sorted(a_list)


# In[ ]:


if __name__ == "__main__":
    
    
    

    random.seed(100)
    
    list_sizes = [500, 1000, 5000]
    
    total_time = 0
    for list_size in list_sizes:
        for i in range(100):
            list_sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            start_sort = time.time()
            ordered_list = python_sort(my_list)
            end_sort = time.time()
            sort_duration = end_sort - start_sort
            total_time += sort_duration
        avg_time = total_time / 100
        print(f"Average time to sort list of {list_size} using Python was {avg_time:0.8f} seconds.")
        
    for list_size in list_sizes:
        for i in range(100):
            list_sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            start_sort = time.time()
            ordered_list = shell_sort(my_list)
            end_sort = time.time()
            sort_duration = end_sort - start_sort
            total_time += sort_duration
        avg_time = total_time / 100
        print(f"Average time to sort list of {list_size} using Insertion sort was {avg_time:0.8f} seconds.") 
    
    for list_size in list_sizes:
        for i in range(100):
            list_sizes = [500, 1000, 5000]
            my_list = get_me_random_list(list_size)
            start_sort = time.time()
            ordered_list = insertion_sort(my_list)
            end_sort = time.time()
            sort_duration = end_sort - start_sort
            total_time += sort_duration
        avg_time = total_time / 100
        print(f"Average time to sort list of {list_size} using Shell sort was {avg_time:0.8f} seconds.")   
    
   
    


# In[ ]:





# In[ ]:





# In[ ]:




