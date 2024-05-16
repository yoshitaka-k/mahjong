import re


class Player:
    __score__ = 0
    __tehai__ = []
    __kawa__ = []
    __meld__ = []


    # 初期化
    def __init__(self):
        self.__score__ = 0
        self.__tehai__ = []
        self.__kawa__ = []
        self.__meld__ = [
            [], [], [], []
        ]


    # スコア追加
    def set_score(self, score):
        self.__score__ = score


    # スコア取得
    def get_score(self):
        return self.__score__


    # 牌追加
    def set_hai(self, hai):
        self.__tehai__.append(hai)


    # 牌取得
    def get_tehai(self, index=None):
        if index is None:
            return self.__tehai__
        else:
            return self.__tehai__[index]


    # 捨牌
    def pop(self, index):
        return self.__tehai__.pop(index)


    # 理牌
    def sort(self):
        pass


    # 河初期化
    def init_kawa(self):
        self.__kawa__ = []


    # 河追加
    def set_kawa(self, kawa):
        self.__kawa__.append(kawa)


    # 河取得
    def get_kawa(self):
        return self.__kawa__


    # 副露
    def set_meld(self, type, hai):
        # ポン
        if type == 'p':
            index = [i for i, x in enurate(self.__tehai__) if x == hai]
            pass

        # チー
        elif type == 'c':
            pass

        # カン
        if type == 'k':
            index = [i for i, x in enurate(self.__tehai__) if x == hai]
            pass


    # 理牌
    def repai(self):
        tehai = []
        m = []
        p = []
        s = []
        k1 = []
        k2 = []
        k3 = []
        k4 = []
        j1 = []
        j2 = []
        j3 = []

        tehai = self.__tehai__
        tehai.sort()

        length = len(tehai)
        for i in range(length):
            if re.search('^m[0-9]', tehai[0]):
                m.append(tehai.pop(0))
            elif re.search('^p[0-9]', tehai[0]):
                p.append(tehai.pop(0))
            elif re.search('^s[0-9]', tehai[0]):
                s.append(tehai.pop(0))
            elif tehai[0] == 'E':
                k1.append(tehai.pop(0))
            elif tehai[0] == 'N':
                k2.append(tehai.pop(0))
            elif tehai[0] == 'W':
                k3.append(tehai.pop(0))
            elif tehai[0] == 'S':
                k4.append(tehai.pop(0))
            elif tehai[0] == 'hk':
                j1.append(tehai.pop(0))
            elif tehai[0] == 'ht':
                j2.append(tehai.pop(0))
            elif tehai[0] == 'tn':
                j3.append(tehai.pop(0))

        self.__tehai__ = m + p + s + k1 + k2 + k3 + k4 + j1 + j2 + j3
