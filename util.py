from node import *

def delete_element(l, index):
    if index == 0:
        return delete_first_element(l)
    elif index == -1 or index - len(l) == -1:
        return delete_last_element(l)
    else:
        return l[0:index] + l[index + 1:]

def delete_first_element(l):
    if len(l) == 1:
        return []
    else:
        return l[1:]

def delete_last_element(l):
    if len(l) == 1:
        return []
    else:
        return l[:-1]
