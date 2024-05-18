import re
import collections

# 面子確認
def mentsu(tehai):
    tehai_copy = tehai.copy()

    split_hai =  __split(tehai_copy)

    # juntu_list = __check_juntu(split_hai)
    kotu_list = __check_kotu(split_hai)
    print('kotu_list: '+str(kotu_list))

    print('# 刻子: '+str(len(kotu_list)))
    # print('# 順子: '+str(len(juntu_list)))


# 刻子確認
def __check_kotu(split_hai):
    cnt = 0
    tmp = ''
    tmp_list = []
    kotu_list = []

    for i in split_hai:
        for hai in i:
            if tmp == hai:
                tmp_list.append(hai)
                cnt = cnt + 1
            else:
                tmp_list = []
                cnt = 0

            if cnt > 2:
                kotu_list.append(tmp_list)
            tmp = hai
    return kotu_list


# 順子確認
def __check_juntu(split_hai):
    del split_hai[3:]
    juntu_cnt = 0

    for i in split_hai:
        length = len(i)
        num_list = []

        for x in range(length):
            num = 0
            cnt = 0
            tmp_list = []

            if x > 0:
                i.pop(0)

            if len(i) > 2:
                for j in i:
                    n = int(re.sub('^m|^p|^s', '', j))

                    if num != 0:
                        if (num+1) == n:
                            if num in num_list:
                                cnt = 0
                            else:
                                if cnt == 0:
                                    tmp_list.append(num)

                                cnt = cnt + 1
                                tmp_list.append(n)
                        elif num == n and cnt > 0:
                            pass
                        else:
                            cnt = 0
                            tmp_list = []
                    num = n

                    num = n

                    if cnt > 1:
                        cnt = 0
                        juntu_cnt = juntu_cnt + 1
                        num_list = num_list + tmp_list
                        tmp_list = []
    return juntu_cnt


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
