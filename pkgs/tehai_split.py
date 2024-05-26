import re

__KAZEHAI = ['E','N','W','S']
__JIHAI = ['hk', 'ht', 'tn']

# 手牌を種類別に分ける
def tehai_split(tehai):
    split_hai = []
    m = []
    p = []
    s = []
    k = []
    j = []

    tehai.sort()
    length = len(tehai)
    for i in range(length):
        if re.search('^m[0-9]', tehai[0]):
            m.append(tehai.pop(0))
        elif re.search('^p[0-9]', tehai[0]):
            p.append(tehai.pop(0))
        elif re.search('^s[0-9]', tehai[0]):
            s.append(tehai.pop(0))
        elif tehai[0] in __KAZEHAI:
            k.append(tehai.pop(0))
        elif tehai[0] in __JIHAI:
            j.append(tehai.pop(0))

    split_hai.append(m)
    split_hai.append(p)
    split_hai.append(s)
    split_hai.append(k)
    split_hai.append(j)

    return split_hai
