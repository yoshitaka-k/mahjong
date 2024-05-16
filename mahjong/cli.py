import random
import libs


_TURN = 0

_CHIICHA_P = 0

_MAHJONG = None

_HAIPAI = None

_PLAYER1 = None
_PLAYER2 = None
_PLAYER3 = None
_PLAYER4 = None


# 配牌
def haipai():
    # 12枚
    for i in range(3):
        for j in range(4):
            k = _CHIICHA_P + j
            if k > 4:
                k = k - 4
            for l in range(4):
                globals()['_PLAYER'+str(k)].set_hai(_MAHJONG.get_yama().pop(0))

    # 13枚
    for i in range(4):
        k = _CHIICHA_P + i
        if k > 4:
            k = k - 4
        globals()['_PLAYER'+str(k)].set_hai(_MAHJONG.get_yama().pop(0))

        # 14枚
        if k == _CHIICHA_P:
            globals()['_PLAYER'+str(k)].set_hai(_MAHJONG.get_yama().pop(0))


# ゲーム処理
def run():
    global _MAHJONG, _TURN

    this_player = _CHIICHA_P
    tehai = _PLAYER1.get_tehai()

    hai = None

    try:
        while True:

            _TURN = _TURN + 1

            if _TURN != 1:
                hai = _MAHJONG.draw()

                print('# TURN: '+str(_TURN)+' / ヤマ牌: '+str(len(_MAHJONG.get_yama()))+' / This PLAYER: '+str(this_player))
                print('# ツモ: '+str(hai))

                if hai is None:
                    print('流局しました。')
                    return

                else:
                    globals()['_PLAYER'+str(this_player)].set_hai(hai)

            else:
                print('# TURN: '+str(_TURN)+' / ヤマ牌: '+str(len(_MAHJONG.get_yama()))+' / This PLAYER: '+str(this_player))


            player_hai = globals()['_PLAYER'+str(this_player)].get_tehai()

            # プレイヤー
            if this_player == 1:
                print('# PLAYER1 配牌: '+str(player_hai))

                print(player_hai)

                # 入力
                value = input('$ Enter an Hai: ')

                # 空エンター
                if value == '':
                    hai = globals()['_PLAYER'+str(this_player)].pop(len(player_hai)-1)
                    globals()['_PLAYER'+str(this_player)].set_kawa(hai)

                else:
                    # 捨て牌選択
                    while (value in player_hai) == False:
                        value = input('$ Enter an Hai: ')

                    hai = globals()['_PLAYER'+str(this_player)].pop(player_hai.index(value))
                    globals()['_PLAYER'+str(this_player)].set_kawa(hai)

                tehai = globals()['_PLAYER'+str(this_player)].get_tehai()

            # CPU
            else:
                # とりあえずツモ切り
                hai = globals()['_PLAYER'+str(this_player)].pop(len(player_hai)-1)
                globals()['_PLAYER'+str(this_player)].set_kawa(hai)

            print('# PLAYER'+str(this_player)+' 捨牌: '+hai)
            print('# PLAYER'+str(this_player)+' 河: '+str(globals()['_PLAYER'+str(this_player)].get_kawa()))

            globals()['_PLAYER'+str(this_player)].repai()

            # ポン確認
            if _MAHJONG.check_pon(tehai, hai):
                globals()['_PLAYER'+str(this_player)].set_meld('p', hai)
                this_player = 1

            # チー確認
            elif _MAHJONG.check_chii(tehai, hai):
                globals()['_PLAYER'+str(this_player)].set_meld('c', hai)
                this_player = 1

            # カン確認
            elif _MAHJONG.check_kan(tehai, hai):
                globals()['_PLAYER'+str(this_player)].set_meld('k', hai)
                this_player = 1

            else:
                this_player = this_player + 1
                if this_player > 4:
                    this_player = 1

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

    for i in range(1, 5):
        # 河初期化
        globals()['_PLAYER'+str(i)].init_kawa()

        # 理牌
        globals()['_PLAYER'+str(i)].repai()

    # ドラ
    _MAHJONG.set_dora()

    # ターン数
    _TURN = 0


# 初期化
def init():
    global _MAHJONG, _HAIPAI, _CHIICHA_P

    _MAHJONG = libs.Mahjong()
    _HAIPAI = libs.Haipai()

    # プレイヤー
    for i in range(1, 5):
        globals()['_PLAYER'+str(i)] = libs.Player()

    # サイ振り決め
    dice = _MAHJONG.dice()

    dice_player = _MAHJONG.chicha(dice)
    print('# サイ振り: _PLAYER'+str(dice_player))

    # 起家決め
    dice = _MAHJONG.dice()

    c = _MAHJONG.chicha(dice)

    c = c + dice_player - 1
    if c > 4:
        c = c - 4
    _CHIICHA_P = c

    print('# 起家: _PLAYER'+str(_CHIICHA_P))


# 処理開始
def main():
    print('------------------------------')

    # 初期化
    init()

    # ゲーム準備
    setup()

    print('# ドラ: '+str(_MAHJONG.get_dora()))
    print('# PLAYER1 配牌: '+str(_PLAYER1.get_tehai()))

    print('------------------------------')

    # ゲーム処理
    run()
