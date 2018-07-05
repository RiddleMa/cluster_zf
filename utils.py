# -*- coding: utf-8 -*-
import pickle
import sys
import pandas as pd


def save_pickle(file_name, input_data):
    with open(file_name, 'wb') as f:
        pickle.dump(input_data, f)


def load_pickle(file_name):
    with open(file_name, 'rb') as f:
        output_data = pickle.load(f)
    return output_data


def word_2_num(list_name, list_word):
    wordMap = dict(zip(list_name, range(len(list_name))))
    list_num = [[wordMap[word] if word in wordMap else word for word in i] for i in list_word]
    return list_num


def num_2_word(list_name, list_num):
    """
    通过list_name生成（0：当归）这样的map，把list_num转成对应的中文
    :param list_name: 所有中药名的list
    :param list_num:以数字组成的list/set/tuple（任意层）
    :return:list_num对应的中文
    """
    # wordMap = dict(zip(range(len(list_name)),list_name))
    wordMap = dict(enumerate(list_name))
    # 使用迭代方法来写
    if isinstance(list_num, (list, tuple, set)):
        newList = list()
        for item in list_num:
            newList.append(num_2_word(list_name, item))
        return newList
    else:
        return wordMap[list_num]


def cut_by_num(list_double, max_num):
    """
    对list每个子list进行删除操作，保留前max_num项
    :param list_double:
    :param max_num:
    :return:
    """
    new_list = list()
    for i, row in enumerate(list_double):
        if len(row) > max_num:
            new_list.append(row[:max_num])
        else:
            new_list.append(row)
    return new_list


def write_csv(name_list, file_path, *args):
    if len(name_list) != len(args):
        print('list长度不对应！')
        sys.exit(1)
    series_list = []
    for i, name in enumerate(name_list):
        column = pd.Series(args[i], name=name)
        series_list.append(column)
    data = pd.concat(series_list, axis=1)
    data = data.sort_values(by=name_list[1], ascending=False)
    data.to_csv(file_path, index=False, encoding='utf-8')
    return data
