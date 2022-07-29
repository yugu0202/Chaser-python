import CHaserConnect
import random

#ゲーム画面で表示される名前を決める
name = "yugu"

"""
自分の移動する方向を決定する変数
2:上 4:左 6:右 8:下
"""
direction = 0

#前回の行動を記録する
before_move = None

#サーバーと通信するためのインスタンスの生成
client = CHaserConnect.Client(name)


#移動するメソッド
def move(direction):
    if direction == 2:
        client.walkUp()
    elif direction == 4:
        client.walkLeft()
    elif direction == 6:
        client.walkRight()
    elif direction == 8:
        client.walkDown()


#ブロックを置くメソッド
def put(direction):
    if direction == 2:
        client.putUp()
    elif direction == 4:
        client.putLeft()
    elif direction == 6:
        client.putRight()
    elif direction == 8:
        client.putDown()


#アイテムを見つけたら方向を記録する
def get_item(values):
    item = []
    for i in range(2,10,2):
        if values[i] == 3:
            item.append(i)

    return item


#動ける方向を記録する
def able_move(values):
    can_move = get_item(values)
    if len(can_move) == 0:
        for i in range(2,10,2):
            if values[i] != 2:
                can_move.append(i)

    return can_move


#動ける方向の配列から方向を決定する
def decision_direction(can_move,before_move):
    if len(can_move) == 1:
        direction = can_move[0]
    elif before_move is None:
        direction = random.choice(can_move)
    else:
        before_move_reverse = 10 - before_move
        if before_move_reverse in can_move:
            can_move.remove(before_move_reverse)
        direction = random.choice(can_move)

    return direction


#敵を見つけたら倒す
def kill(values):
    for i in range(2,10,2):
        if values[i] == 1:
            put(i)


while True: # ここからループ
    values = client.getReady() # サーバーに行動準備が完了したと伝える
    if values[0] == 0:
        break

    kill(values)

    can_move = able_move(values)

    direction = decision_direction(can_move, before_move)

    move(direction)
    before_move = direction

    if values[0] == 0:
        break
