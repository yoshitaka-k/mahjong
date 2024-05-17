import random


class Mahjong:
    __yama__ = []
    __wanpai__ = []
    __dora__ = []


    # 初期化
    def __init__(self):
        __yama__ = []
        __wanpai__ = []
        __dora__ = []


    # サイ振り
    def dice(self):
        dice = [
            random.randrange(1, 7),
            random.randrange(1, 7)
        ]
        return sum(dice)


    # サイ振り・起家決め
    def chicha(self, dice):
        l = 0
        for i in range(1, dice+1):
            l = i
            if i > 8:
                l = i - 8
            elif i > 4:
                l = i - 4
        return l


    # 山積み
    def init_yama(self):
        yama = []

        for l in range(4): # 萬子
            for i in range(1, 10):
                yama.append('m'+str(i))
        for l in range(4): # 筒子
            for i in range(1, 10):
                yama.append('p'+str(i))
        for l in range(4): # 索子
            for i in range(1, 10):
                yama.append('s'+str(i))

        for l in range(4):
            yama.append('E')
        for l in range(4):
            yama.append('N')
        for l in range(4):
            yama.append('W')
        for l in range(4):
            yama.append('S')

        for l in range(4):
            yama.append('hk')
        for l in range(4):
            yama.append('ht')
        for l in range(4):
            yama.append('tn')

        for i in range(5): # 洗牌
            random.shuffle(yama)
            pass

        self.__yama__ = yama


    # 王牌
    def init_wanpai(self):
        for i in range(14):
            self.__wanpai__.append(self.__yama__.pop(0))


    # ヤマ取得
    def get_yama(self):
        return self.__yama__


    # 王牌
    def get_wanpai(self):
        return self.__wanpai__


    # ドラ表示牌設定
    def set_dora(self):
        self.__dora__ = self.__wanpai__.pop(0)


    # ドラ表示牌設定
    def get_dora(self):
        return self.__dora__


    # ツモ
    def draw(self):
        hai = None

        if len(self.__yama__) > 0:
            hai = self.__yama__.pop(0)

        return hai


    # ポン確認
    def check_pon(self, tehai, hai):
        if tehai.count(hai) == 2:
            value = input('ポンしますか？[y/N]: ')
            if value == '' or value == 'n' or value == 'N':
                return False
            else:
                return True


    # チー確認
    def check_chii(self, tehai, hai):
        pass


    # カン確認
    def check_kan(self, tehai, hai):
        if tehai.count(hai) == 3:
            value = input('カンしますか？[y/N]: ')
            if value == '' or value == 'n' or value == 'N':
                return False
            else:
                return True
