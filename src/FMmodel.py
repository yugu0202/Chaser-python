import CHaserConnect
import random

#ゲーム画面で表示される名前を決める
name = "yugu"

"""
自分の移動する方向を決定する変数
0:上 1:右 2:下 3:左
"""
direction = 0

#サーバーと通信するためのインスタンスの生成
client = CHaserConnect.Client(name)

def random_direction():
    direction = random.randint(0,4)
    return direction

def action(direction):
    if direction == 0:
        values = client.walkUp()
    else if direction == 1:
        values = client.walkRight()
    else if direction == 2:
        values = client.walkDown()
    else if direction == 3:
        values = client.walkLeft()

    return values


while True: # ここからループ
    values = client.getReady() # サーバーに行動準備が完了したと伝える
    if values[0] == 0:
        break

    direction = random_direction()
    values = action(direction)

    if values[0] == 0:
        break
