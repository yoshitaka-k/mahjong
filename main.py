import random
from player import Player


_CHIICHA = 0

_YAMA = []
_WANPAI = []
_DORA = []

_PLAYER1 = None
_PLAYER2 = None
_PLAYER3 = None
_PLAYER4 = None


# 配牌
def haipai():
    global _YAMA

    # 12枚
    for i in range(3):
        for j in range(4):
            k = _CHIICHA + j
            if k > 4:
                k = k - 4
            for l in range(4):
                globals()['_PLAYER'+str(k)].set_hai(_YAMA.pop(0))

    # 13枚
    for i in range(4):
        k = _CHIICHA + i
        if k > 4:
            k = k - 4
        globals()['_PLAYER'+str(k)].set_hai(_YAMA.pop(0))

        # 14枚
        if k == _CHIICHA:
            globals()['_PLAYER'+str(k)].set_hai(_YAMA.pop(0))


# 王牌
def wanpai():
    global _YAMA, _WANPAI

    for i in range(14):
        _WANPAI.append(_YAMA.pop(0))


# サイ振り・起家決め
def start_player(dice):
    l = 0
    for i in range(1, dice+1):
        l = i
        if i > 8:
            l = i - 8
        elif i > 4:
            l = i - 4
    return l


# サイ振り
def dice_shuffle():
    dice = [
        random.randrange(1, 7),
        random.randrange(1, 7)
    ]
    return sum(dice)


# ヤマ積み
def yamadumi():
    global _YAMA

    yama = []

    for i in range(1, 10): # 萬子
        for l in range(4):
            yama.append('m'+str(i))
    for i in range(1, 10): # 筒子
        for l in range(4):
            yama.append('p'+str(i))
    for i in range(1, 10): # 索子
        for l in range(4):
            yama.append('s'+str(i))

    for l in range(4):
        yama.append('e')
    for l in range(4):
        yama.append('n')
    for l in range(4):
        yama.append('w')
    for l in range(4):
        yama.append('s')

    for l in range(4):
        yama.append('hk')
    for l in range(4):
        yama.append('ht')
    for l in range(4):
        yama.append('tn')

    for i in range(0, 5): # 洗牌
        random.shuffle(yama)

    _YAMA = yama


# ゲーム準備
def setup():
    global _WANPAI, _DORA

    # ヤマ積む
    yamadumi()

    # 王牌
    wanpai()

    # 配牌
    haipai()

    # 理牌
    for i in range(1, 5):
        globals()['_PLAYER'+str(i)].repai()

    # ドラ
    _DORA = _WANPAI.pop(0)


# 初期化
def init():
    global _CHIICHA

    # プレイヤー
    for i in range(1, 5):
        globals()['_PLAYER'+str(i)] = Player()

    # サイ振り決め
    dice = dice_shuffle()
    print('DICE: '+str(dice))

    dice_player = start_player(dice)
    print('サイ振り: _PLAYER'+str(dice_player))

    # 起家決め
    dice = dice_shuffle()
    print('DICE: '+str(dice))

    chiha = start_player(dice)

    chiha = chiha + dice_player - 1
    if chiha > 4:
        chiha = chiha - 4
    _CHIICHA = chiha

    print('起家: _PLAYER'+str(_CHIICHA))


if __name__ == '__main__':
    # 初期化
    init()

    # ゲーム準備
    setup()

    print('ヤマ数:'+str(len(_YAMA)))
    print('王牌数:'+str(len(_WANPAI)))
    print('ドラ: '+str(_DORA))

    print('PLAYER1 配牌')
    print(_PLAYER1.get_hai())
