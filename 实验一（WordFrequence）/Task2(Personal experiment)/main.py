#!/usr/bin/env python
# coding: utf-8


import string
import sys
import re
import os

# nlp
# pip install -U textblob
# python -m textblob.download_corpora
from textblob import TextBlob
from textblob import Word


# # 第0步


def get_letter(path, letter=[]):
    with open(path, 'r', encoding='ASCII', errors='ignore') as f:
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
    letter = sorted(letter_dic.items(), key=lambda e: e[1], reverse=True)
    return letter, count_en


def zero_one(path):
    letter, count_en = get_letter(path)
    for x in letter:
        print(x[0] + ':' + str(x[1] / count_en * 100) + '%')


# # 第一步

# ## 功能1


def get_word(path):  # return one list
    with open(path, 'r', encoding='ASCII', errors='ignore') as f:
        lines = f.readlines()
    f.close()

    word_dic = {}
    count_en = 0
    for line in lines:
        s = re.split(r'\W+', line)
        s = [word.lower() for word in s if len(word) > 0]
        for x in s:
            if x not in word_dic:
                word_dic[x] = 0
            word_dic[x] += 1
            count_en += 1
    word = sorted(word_dic.items(), key=lambda e: e[1], reverse=True)
    return word, count_en


def one_one(path):
    word, _ = get_word(path)
    for x in word:
        print(x[0], end=' ')
    print('\n')


# ## 功能2


def get_file(root_path, _files=[]):
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):  # not a dir
            _files.append(root_path + '/' + file)
    return _files


def get_all_file(root_path, all_files=[]):
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):  # not a dir
            all_files.append(root_path + '/' + file)
        else:  # is a dir
            get_all_file((root_path + '/' + file), all_files)
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


# ## 功能3


def one_three(path, n=None):
    word, count_en = get_word(path)
    if n is None:
        for x in word:
            print(x[0] + ':' + str(x[1] / count_en * 100) + '%')
    else:
        for i in range(n):
            print(word[i][0] + ':' + str(word[i][1] / count_en * 100) + '%')


# # 第二步

# ## 功能4


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
        print(x[0], end=' ')


# # 第3步

# ## 功能5


def get_phrase(path, n, phrase=[]):
    with open(path, 'r', encoding='ASCII', errors='ignore') as f:
        lines = f.readlines()
    f.close()

    phrase_dic = {}
    count_en = 0
    for line in lines:
        blob = TextBlob(line)
        for x in blob.noun_phrases:
            s = re.split(r'\W+', x)
            s = [word.lower() for word in s if len(word) > 0]
            if len(s) != n:
                continue
            if x not in phrase_dic:
                phrase_dic[x] = 0
            phrase_dic[x] += 1
            count_en += 1
    phrase = sorted(phrase_dic.items(), key=lambda e: e[1], reverse=True)
    return phrase, count_en


def three_five(path, n):
    phrase, count_en = get_phrase(path, n)
    for x in phrase:
        print(x[0] + ':' + str(x[1] / count_en * 100) + '%')


# # 第四步

# ## 功能6


def get_prototype(path, prototype=[]):
    word, count_en = get_word(path)
    prototype_dic = {}
    for x in word:
        w = Word(x[0])
        w = w.lemmatize("v")
        if w not in prototype_dic:
            prototype_dic[w] = 0
        prototype_dic[w] += x[1]
    prototype = sorted(prototype_dic.items(), key=lambda e: e[1], reverse=True)
    return prototype, count_en


def four_six(path):
    prototype, count_en = get_prototype(path)
    for x in prototype:
        print(x[0] + ':' + str(x[1] / count_en * 100) + '%')


def transfer():
    # print("程序支持功能与输入格式请输入 ’-help‘ 查看")
    if sys.argv[1] == '-c' and len(sys.argv) == 3:
        print("输出文件中某个英文文本文件中 26 字母出现的频率")
        zero_one(sys.argv[2])
    elif sys.argv[1] == '-f' and len(sys.argv) == 3:
        print("输出文件中所有不重复的单词")
        one_one(sys.argv[2])
    elif sys.argv[1] == '-d':
        if len(sys.argv) == 4 and sys.argv[2] == '-s':
            print("输出指定文件目录以及子目录每一个文件中所有不重复的单词")
            one_two_two(sys.argv[2])
        elif len(sys.argv) == 3:
            print("输出指定文件目录下每一个文件中所有不重复的单词")
            one_two_one(sys.argv[2])
    elif sys.argv[1] == '-n':
        print("输出文件中的前 N 个最常出现的英语单词(如果不指定 N ,则输出所有英语单词)")
        if len(sys.argv) == 3:
            one_three(sys.argv[2])
        elif len(sys.argv) == 4:
            one_three(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == '-x' and len(sys.argv) == 5:
        print("输出文件中不在停词表中的不重复英语单词")
        two_four(sys.argv[2], sys.argv[4])
    elif sys.argv[1] == '-p' and len(sys.argv) == 4:
        print("输出文件中英语词组(nlp实现，如果文件过大，需要稍微等待)")
        three_five(sys.argv[2], int(sys.argv[3]))
    elif sys.argv[1] == '-v' and len(sys.argv) == 3:
        print("输出文件中英语单词原型(nlp实现，如果文件过大，需要稍微等待)")
        four_six(sys.argv[2])
    elif sys.argv[1] == '-help' and len(sys.argv) == 2:
        print("main.exe -c <file name>  --输出文件中某个英文文本文件中 26 字母出现的频率")
        print("main.exe -f <file name>  --输出文件中所有不重复的单词")
        print("main.exe -d <directory name>  --输出指定文件目录下每一个文件中所有不重复的单词")
        print("main.exe -d -s <directory name>  --输出指定文件目录下每一个文件中所有不重复的单词")
        print("main.exe -n <file name> <number>  --输出文件中的前 N 个最常出现的英语单词(如果不指定 N ,则输出所有英语单词)")
        print("main.exe -p <file name> <number>  --输出文件中英语词组(nlp实现，如果文件过大，需要稍微等待)")
        print("main.exe -v <file name>  --输出文件中英语单词原型(nlp实现，如果文件过大，需要稍微等待)")
    else:
        print("输入参数错误！请重新输入(-help查看帮助文档)")


transfer()
