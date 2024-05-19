from mahjong.setting import _NUM_OF_PLAYER
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
        print('# サイの目: '+str(dice))

        j = 0
        for i in range(1, (dice+1)):
            j = i

            while j > _NUM_OF_PLAYER:
                j = j - _NUM_OF_PLAYER

        return j


    # 山積み
    def init_yama(self):
        yama = []

        for i in range(9):
            yama.extend(['m'+str(i+1)] * 4)
            yama.extend(['p'+str(i+1)] * 4)
            yama.extend(['s'+str(i+1)] * 4)

        yama.extend(['E'] * 4)
        yama.extend(['N'] * 4)
        yama.extend(['W'] * 4)
        yama.extend(['S'] * 4)

        yama.extend(['hk'] * 4)
        yama.extend(['ht'] * 4)
        yama.extend(['tn'] * 4)

        for i in range(5):
            random.shuffle(yama)

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
    def check_pon(self, current, tehai, hai):
        if tehai.count(hai) == 2:
            if current == 1:
                value = input('ポンしますか？[y/N]: ')
                if value == '' or value == 'n' or value == 'N':
                    return False
                else:
                    return True
            else:
                pass


    # チー確認
    def check_chii(self, current, tehai, hai):
        pass


    # カン確認
    def check_kan(self, current, tehai, hai):
        if tehai.count(hai) == 3:
            if current == 1:
                value = input('カンしますか？[y/N]: ')
                if value == '' or value == 'n' or value == 'N':
                    return False
                else:
                    return True
            else:
                pass
