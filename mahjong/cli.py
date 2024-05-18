from mahjong.setting import _NUM_OF_PLAYER

import random
import libs
import pkgs


# 変数
_TURN = 0

_CHIICHA_P = 0

_MAHJONG = None

_PLAYER1 = None
_PLAYER2 = None
_PLAYER3 = None
_PLAYER4 = None


# プレイヤー処理
def run_player(current):
    tehai = globals()['_PLAYER'+str(current)].get_tehai()

    # CPU処理
    if current != 1:
        # とりあえずツモ切り
        hai = globals()['_PLAYER'+str(current)].pop(len(tehai)-1)
        globals()['_PLAYER'+str(current)].set_kawa(hai)

    # プレイヤー処理
    else:
        # 入力
        value = input('$ Enter an Hai: ')

        # 空エンター
        if value == '':
            hai = _PLAYER1.pop(len(tehai)-1)
            _PLAYER1.set_kawa(hai)

        else:
            # 捨て牌選択
            while (value in tehai) == False:
                value = input('$ Enter an Hai: ')

            hai = _PLAYER1.pop(tehai.index(value))
            _PLAYER1.set_kawa(hai)

        print('# PLAYER'+str(current)+' 捨牌: '+hai)
        print('# PLAYER'+str(current)+' 河: '+str(_PLAYER1.get_kawa()))

    return hai


# 配牌
def haipai():
    yama = _MAHJONG.get_yama()

    # 取る順番
    pliyer_list = []
    for i in range(_NUM_OF_PLAYER):
        p = _CHIICHA_P + i
        if p > _NUM_OF_PLAYER:
            p = p - _NUM_OF_PLAYER
        pliyer_list.append(p)

    # 12枚
    for l in range(3):
        for p in pliyer_list:
            for l in range(4):
                globals()['_PLAYER'+str(p)].set_hai(yama.pop(0))

    # 13枚
    for p in pliyer_list:
        globals()['_PLAYER'+str(p)].set_hai(yama.pop(0))

        # 14枚
        if p == _CHIICHA_P:
            globals()['_PLAYER'+str(p)].set_hai(yama.pop(0))


# ゲーム処理
def run():
    global _MAHJONG, _TURN

    current = _CHIICHA_P
    tehai = _PLAYER1.get_tehai()

    draw_hai = None

    try:
        while True:

            _TURN = _TURN + 1

            # 2ターン目以上ツモ
            if _TURN > 1:
                draw_hai = _MAHJONG.draw()

            print('# TURN: '+str(_TURN)+' / This PLAYER: '+str(current))
            print('# ヤマ牌: '+str(len(_MAHJONG.get_yama()))+' / ドラ表示牌: '+str(_MAHJONG.get_dora()))

            if _TURN > 1:
                print('# ツモ: '+str(draw_hai))

                if draw_hai is None:
                    print('流局しました。')
                    return

                else:
                    globals()['_PLAYER'+str(current)].set_hai(draw_hai)

            tehai = globals()['_PLAYER'+str(current)].get_tehai()

            print('# PLAYER'+str(current)+' 配牌: '+str(tehai))

            # 手牌確認
            pkgs.mentsu(tehai)

            # プレイヤー処理
            sutehai = run_player(current)
            tehai = globals()['_PLAYER'+str(current)].get_tehai()


            tehai = globals()['_PLAYER'+str(current)].get_tehai()

            globals()['_PLAYER'+str(current)].repai()

            # ポン確認
            if _MAHJONG.check_pon(current, tehai, sutehai):
                globals()['_PLAYER'+str(current)].set_meld('p', sutehai)
                current = 1

            # チー確認
            elif _MAHJONG.check_chii(current, tehai, sutehai):
                globals()['_PLAYER'+str(current)].set_meld('c', sutehai)
                current = 1

            # カン確認
            elif _MAHJONG.check_kan(current, tehai, sutehai):
                globals()['_PLAYER'+str(current)].set_meld('k', sutehai)
                current = 1

            else:
                current = current + 1
                if current > _NUM_OF_PLAYER:
                    current = 1

            print('------------------------------')

    except KeyboardInterrupt:
        print('入力中断')


# ゲーム準備
def setup():
    global _MAHJONG, _TURN

    # ヤマ積む
    _MAHJONG.init_yama()

    # 王牌
    _MAHJONG.init_wanpai()

    # 配牌
    haipai()

    for i in range(_NUM_OF_PLAYER):
        # 河初期化
        globals()['_PLAYER'+str(i+1)].init_kawa()

        # 理牌
        globals()['_PLAYER'+str(i+1)].repai()

    # ドラ
    _MAHJONG.set_dora()

    # ターン数
    _TURN = 0


# 初期化
def init():
    global _MAHJONG, _CHIICHA_P

    _MAHJONG = libs.Mahjong()

    # プレイヤー
    for i in range(_NUM_OF_PLAYER):
        globals()['_PLAYER'+str(i+1)] = libs.Player()

    # サイ振り決め
    dice = _MAHJONG.dice()

    dice_player = _MAHJONG.chicha(dice)
    print('# サイ振り: PLAYER'+str(dice_player))

    # 起家決め
    dice = _MAHJONG.dice()

    c = _MAHJONG.chicha(dice)

    c = c + dice_player - 1
    if c > _NUM_OF_PLAYER:
        c = c - _NUM_OF_PLAYER
    _CHIICHA_P = c

    print('# 起家: PLAYER'+str(_CHIICHA_P))


# 処理開始
def main():
    print('==============================')
    print('# プレイ人数: '+str(_NUM_OF_PLAYER) +'人')

    # 初期化
    init()

    # ゲーム準備
    setup()

    print('# ドラ: '+str(_MAHJONG.get_dora()))
    # print('# PLAYER1 配牌: '+str(_PLAYER1.get_tehai()))

    print('==============================')

    # ゲーム処理
    run()
