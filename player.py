import re

class Player:
    __score__ = 0
    __hai__ = []
    __kawa__ = []

    # 初期化
    def __init__(self):
        self.__score__ = 0
        self.__hai__ = []
        self.__kawa__ = []

    # スコア追加
    def set_score(self, score):
        self.__score__ = score

    # スコア取得
    def get_score(self):
        return self.__score__

    # 牌追加
    def set_hai(self, hai):
        self.__hai__.append(hai)

    # 牌取得
    def get_hai(self):
        return self.__hai__

    # 理牌
    def sort(self):
        pass

    # 河追加
    def set_kawa(self, kawa):
        self.__kawa__ = kawa

    # 河取得
    def get_kawa(self):
        return self.__kawa__

    # 理牌
    def repai(self):
        hai = []
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

        hai = self.__hai__
        hai.sort()

        length = len(hai)
        for i in range(length):
            if re.search('^m[0-9]', hai[0]):
                m.append(hai.pop(0))
            elif re.search('^p[0-9]', hai[0]):
                p.append(hai.pop(0))
            elif re.search('^s[0-9]', hai[0]):
                s.append(hai.pop(0))
            elif hai[0] == 'e':
                k1.append(hai.pop(0))
            elif hai[0] == 'n':
                k2.append(hai.pop(0))
            elif hai[0] == 'w':
                k3.append(hai.pop(0))
            elif hai[0] == 's':
                k4.append(hai.pop(0))
            elif hai[0] == 'hk':
                j1.append(hai.pop(0))
            elif hai[0] == 'ht':
                j2.append(hai.pop(0))
            elif hai[0] == 'tn':
                j3.append(hai.pop(0))

        self.__hai__ = m + p + s + k1 + k2 + k3 + k4 + j1 + j2 + j3
