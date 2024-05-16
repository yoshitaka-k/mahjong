import re
import collections

class Haipai(object):
    __tehai__ = []
    __split__ = []


    # 初期化
    def __init__(self):
        self.__tehai__ = []


    # 配牌確認
    def check(self, tehai):
        self.__tehai__ = tehai

        self.split()

        self.check_juntu()
        self.check_kotu()


    # 順子確認
    def check_juntu(self):
        print('# 順子確認')
        for i in self.__split__:
            print(i)
        pass


    # 刻子確認
    def check_kotu(self):
        print('# 刻子確認')
        for i in self.__split__:
            print(i)
        pass


    def split(self):
        tehai = self.__tehai__

        m = []
        p = []
        s = []
        k = []
        j = []

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

        self.__split__.append(m)
        self.__split__.append(p)
        self.__split__.append(s)
        self.__split__.append(k)
        self.__split__.append(j)

