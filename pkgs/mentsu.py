import re
import collections
from pkgs.tehai_split import tehai_split


# 面子確認
def check_mentsu(tehai):
    result = []
    tehai_copy = tehai.copy()

    split_hai =  tehai_split(tehai_copy)

    janto_list = __check_janto(split_hai)
    kotu_list  = __check_kotu(split_hai)
    juntu_list = __check_juntu(split_hai)

    print('# 雀頭: '+str(janto_list))
    print('# 刻子: '+str(kotu_list))
    print('# 順子: '+str(juntu_list))

    result.append(janto_list)
    result.append(kotu_list)
    result.append(juntu_list)

    return result


# 面子数
def number_of_mentsu(mentsu_list):
    cnt = 0
    janto, kotu, juntu = mentsu_list

    if len(janto) == 1:
        cnt = cnt + 1

    cnt = cnt + len(kotu)

    for l in juntu:
        j = []
        for i in l:
            if i not in janto and i not in kotu:
                j.append(i)

        if len(j) == 9:
            cnt = cnt + 3
        elif len(j) > 5:
            cnt = cnt + 2
        elif len(j) > 2:
            cnt = cnt + 1

    return cnt


# 雀頭確認
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

    for hai_list in split_hai:
        cnt = 0
        tmp = 0
        tmp_list = []

        if len(hai_list) < 3:
            continue

        try:
            index = 0
            for hai in hai_list:
                a, b = hai[:1], int(hai[1:])
                if (tmp == 0):
                    tmp = b
                    index = index + 1
                    continue

                if b == (tmp+1):
                    if cnt == 0:
                        tmp_list.append(hai_list[index-1])

                    tmp_list.append(hai)
                    cnt = cnt + 1

                elif b == tmp and cnt > 0:
                    pass

                else:
                    if len(tmp_list) > 2:
                        juntu_list.append(tmp_list)

                    cnt = 0
                    tmp_list = []

                tmp = b
                index = index + 1

            if len(tmp_list) > 2:
                juntu_list.append(tmp_list)

        except IndexError:
            print('配列終わり')

    return juntu_list
