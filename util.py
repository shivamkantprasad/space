from random import randint


def RGB(color):
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    a = 255
    if len(color) == 9:
        a = int(color[7:9], 16)
    return r, g, b, a


def mapThis(current, min1, max1, min2, max2):
    x = min1
    max1 -= x
    current -= x
    x = min2
    max2 -= x
    out = (current / max1) * max2
    out += x + 1
    max2 += x
    if out < min2:
        out = min2
    elif out > max2:
        out = max2
    return out


def listsub(list1, list2):
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x] - list2[x])
    return list3


def listdivied(list1, x):
    if x != 0:
        list3 = []
        for y in range(len(list1)):
            list3.append(list1[y] / x)
        return list3
    print('Divied By 0')
    return list1


def listadd(list1, list2):
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x] + list2[x])
    return list3


def clamp(num, minnum, maxnum):
    res = min(max(num, minnum), maxnum)
    return res


def listloop(list1, loopby):
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x] % loopby[x])
    return list3


def randColor():
    R = randint(0, 200)
    G = randint(0, 200)
    B = randint(0, 250)
    return (R, G, B)
