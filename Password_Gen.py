#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calls a list of words from a json file
import json
with open('words_dictionary.json') as words_dic:
    python_dict = json.load(words_dic)


# In[2]:


#Turns the dictionary file into a list
dict_list = list(python_dict.keys())
#print(dict_list[1])


# In[3]:


#Removes any word from the list that is under 4 letters
def clear_list(word_size, input_list):
    cleared_list = []
    cleared_list = [word for word in input_list if len(word) >= word_size]
    return cleared_list
cull_dict = clear_list(5, dict_list)
#print(cull_dict[1])


# In[4]:


#Generates a random number, reads that entry and puts into a variable (function)
import random
def random_word_generator():
    random_number = random.randint(0, len(cull_dict))
    random_word = cull_dict[random_number]
    return random_word


first_word = random_word_generator()
#print(first_word)
second_word = random_word_generator()
#print(second_word)


# In[5]:


#Converts it into a string and slices it into 4 letters and capitalises the first word (function)
def trim_password(word_size, password):
    trimmed_password = password[0:word_size]
    return trimmed_password

first_password = trim_password(4, first_word)
capitalised_first_password = first_password.title()
#print(capitalised_first_password)


# In[6]:


#Repeats process with the second half and appends it to the first (using function)
second_password = trim_password(4, second_word)
third_password = capitalised_first_password + second_password
#print(third_password)


# In[7]:


#Generates a random number between 10 and 99 and appends it.
random_number_2 = random.randint(10, 99)
fourth_password = third_password + str(random_number_2)
#print(fourth_password)


# In[8]:


#Adds a random special character to the end (!?#*)
special_chars = '!?#*'
random_number_3 = random.randint(0, 3)
fifth_password = fourth_password + special_chars[random_number_3]
print(fifth_password)


# In[1]:


#Keeps the prorgam open at the end
input("Press enter to exit...")


# In[ ]:




