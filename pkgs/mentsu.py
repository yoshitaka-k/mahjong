import re
import collections


# 面子確認
def mentsu(tehai):
    tehai_copy = tehai.copy()

    split_hai =  __split(tehai_copy)

    janto_list = __check_janto(split_hai)
    kotu_list = __check_kotu(split_hai)
    kantu_list = __check_kantu(split_hai)
    juntu_list = __check_juntu(split_hai)

    print('# 雀頭: '+str(janto_list))
    print('# 刻子: '+str(kotu_list))
    print('# 槓子: '+str(kantu_list))
    print('# 順子: '+str(juntu_list))


# 雀頭確認（刻子2個確認）
def __check_janto(split_hai):
    result = []

    for i in split_hai:
        cnt_list = collections.Counter(i)

        if 2 in cnt_list.values():
            for k in cnt_list:
                if cnt_list[k] == 2:
                    result.append(k)

    return result


# 刻子確認
def __check_kotu(split_hai):
    result = []

    for i in split_hai:
        cnt_list = collections.Counter(i)

        if 3 in cnt_list.values():
            for k in cnt_list:
                if cnt_list[k] == 3:
                    result.append(k)

    return result


# 槓子確認
def __check_kantu(split_hai):
    result = []

    for i in split_hai:
        cnt_list = collections.Counter(i)

        if 4 in cnt_list.values():
            for k in cnt_list:
                if cnt_list[k] == 4:
                    result.append(k)

    return result


# 順子確認
def __check_juntu(split_hai):
    # 字牌除去
    del split_hai[3:]

    juntu_list = []

    for i in split_hai:
        tmp_list = []
        num_list = []

        length = len(i)
        for x in range(length):
            cnt = 0
            tmp = 0
            tmp_list = []

            if x > 0:
                i.pop(0)

            if len(i) < 3:
                continue

            try:
                index = 0
                for hai in i:
                    a, b = hai[:1], int(hai[1:])
                    if (tmp == 0):
                        tmp = b
                        index = index + 1
                        continue

                    if b == (tmp+1):
                        if cnt == 0:
                            tmp_list.append(i[index-1])

                        tmp_list.append(hai)
                        cnt = cnt + 1
                    elif b == tmp and cnt > 0:
                        pass
                    else:
                        cnt = 0
                        tmp_list = []

                    tmp = b

                    if cnt > 1:
                        if tmp_list not in juntu_list:
                            juntu_list.append(tmp_list)

                        cnt = 0
                        tmp_list = []

                    index = index + 1

            except IndexError:
                print('配列終わり')

    length = len(juntu_list)
    if length < 2:
        return juntu_list

    return juntu_list


# 種類別に分割
def __split(tehai):
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
        elif tehai[0] == 'E' or tehai[0] == 'N' or tehai[0] == 'W' or tehai[0] == 'S':
            k.append(tehai.pop(0))
        elif tehai[0] == 'hk' or tehai[0] == 'ht' or tehai[0] == 'tn':
            j.append(tehai.pop(0))

    split_hai.append(m)
    split_hai.append(p)
    split_hai.append(s)
    split_hai.append(k)
    split_hai.append(j)

    return split_hai
