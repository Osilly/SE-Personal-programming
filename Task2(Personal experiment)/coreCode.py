#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import string
import sys
import re
import os


# # 第0步

# In[2]:


def get_letter(path, letter=[]):
    with open(path, 'r', encoding='gb18030', errors='ignore') as f:
        lines = f.readlines()
    f.close()
    letter_dic = {}
    count_en = 0
    for line in lines:
        for s in line:
            if s in string.ascii_letters:
                if s not in letter_dic:
                    letter_dic[s] = 0
                letter_dic[s] += 1
                count_en += 1
    letter = sorted(letter_dic.items(), key=lambda e:e[1], reverse=True)
    return letter, count_en


# In[3]:


def zero_one(path):
    letter, count_en = get_letter(path)
    for x in letter:
        print(x[0]+':'+str(x[1]/count_en))


# In[4]:


# test
zero_one("C:/Users/柠檬/Desktop/test/one.txt")


# In[5]:


if sys.argv[0] == '-c' and len(sys.argv) == 2:
    zero_one(sys.argv)


# # 第一步

# ## 功能1

# In[6]:


def get_word(path): #return one list
    with open(path, 'r', encoding='gb18030', errors='ignore') as f:
        lines = f.readlines()
    f.close()
    
    word_dic = {}
    count_en = 0
    for line in lines:
        s = re.split(r'\W+',line)
        s = [word.lower() for word in s if len(word) > 0]
        for x in s:
            if x not in word_dic:
                word_dic[x] = 0
            word_dic[x] += 1
            count_en += 1
    word = sorted(word_dic.items(), key=lambda e:e[1], reverse=True)
    return word, count_en

def one_one(path):
    word, _ = get_word(path)
    for x in word:
        print(x[0],end=' ')
    print('\n')


# In[7]:


# test
one_one("C:/Users/柠檬/Desktop/test/one.txt")


# In[8]:


# 调用
if sys.argv[0] == '-f':
    one_one(sys.argv[1]) 


# ## 功能2

# In[9]:


def get_file(root_path,_files=[]):
    files = os.listdir(root_path)
    for file in files:  
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            _files.append(root_path + '/' + file)
    return _files

def get_all_file(root_path,all_files=[]):
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            all_files.append(root_path + '/' + file)
        else:  # is a dir
            get_all_file((root_path+'/'+file),all_files)
    return all_files

def one_two_one(root_path):
    paths = get_file(root_path)
    for path in paths:
        print(path)
        one_one(path)  

def one_two_two(root_path):
    paths = get_all_file(root_path)
    for path in paths:
        print(path)
        one_one(path)  


# In[10]:


# test
one_two_one("C:/Users/柠檬/Desktop/test")


# In[11]:


# test
one_two_two("C:/Users/柠檬/Desktop/test")


# In[12]:


# 调用
if sys.argv[0] == '-d':
    if len(sys.argv) >= 2 and sys.argv[1] == '-s':
        root_path = sys.argv[2] 
        one_two(sys.argv[2])
    elif len(sys.argv) == 2:
        root_path = sys.argv[1] 
        one_two(sys.argv[1])  


# ## 功能3

# In[13]:


def one_three(path, n=None):
    word, count_en = get_word(path)
    if n == None:        
        for x in word:
            print(x[0]+':'+str(x[1]/count_en))
    else:
        for i in range(n):
            print(word[i][0]+':'+str(word[i][1]/count_en))


# In[14]:


# test
one_three("C:/Users/柠檬/Desktop/test/one.txt")


# In[15]:


# test
one_three("C:/Users/柠檬/Desktop/test/one.txt",10)


# In[16]:


# 调用
if sys.argv[0] == '-n':
    path = sys.argv[1] 
    if len(sys.argv) == 2:
        one_three(sys.argv[1])
    elif len(sys.argv) == 3:
        one_three(sys.argv[1], sys.argv[2])


# # 第二步

# ## 功能4

# In[17]:


def get_wordstop(stopword_path):
    return get_word(stopword_path) 
    
def get_skipedword(stopword_path, path):
    word, count_en = get_word(stopword_path)
    wordstop, _ = get_wordstop(path)
    skipedword = []
    for x in word:
        if x[0] in word[:][0]:
            count_en -= 1
            continue
        skipedword.append(x)
    return skipedword, count_en

def two_four(stopword_path, path):
    wordstop, count_en = get_skipedword(stopword_path, path)
    for x in wordstop:
        print(x[0], end = ' ')


# In[18]:


# test
two_four(r"C:\Users\柠檬\Desktop\test\stopwords_en.txt",r"C:\Users\柠檬\Desktop\test\one.txt")


# In[19]:


# 调用
if sys.argv[0] == '-n' and len(sys.argv) == 4:
    stopword_path = sys.argv[1] 
    path = sys.argv[3]
    two_four(stopword_path, path)


# # 第3步

# ## 功能5

# In[20]:


# pip install -U textblob
# python -m textblob.download_corpora
from textblob import TextBlob


# In[21]:


def get_phrase(path, n, phrase=[]):
    with open(path, 'r', encoding='gb18030', errors='ignore') as f:
        lines = f.readlines()
    f.close()
    
    phrase_dic = {}
    count_en = 0
    for line in lines:
        blob = TextBlob(line)
        for x in blob.noun_phrases:
            s = re.split(r'\W+',x)
            s = [word.lower() for word in s if len(word) > 0]
            if len(s) != n:
                continue
            if x not in phrase_dic:
                phrase_dic[x] = 0
            phrase_dic[x] += 1
            count_en += 1
    phrase = sorted(phrase_dic.items(), key=lambda e:e[1], reverse=True)
    return phrase, count_en

def three_five(path, n):
    phrase, count_en = get_phrase(path, n)
    for x in phrase:
        print(x[0]+':'+str(x[1]/count_en))


# In[22]:


# test
three_five("C:/Users/柠檬/Desktop/test/one.txt", 2)


# In[23]:


# 调用
if sys.argv[0] == '-n' and len(sys.argv) == 2:
    two_four(sys.argv[0], sys.argv[1])


# # 第四步

# ## 功能6

# In[ ]:




