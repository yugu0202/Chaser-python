import CHaserConnect

name = "yugu"
values = [] # フィールド情報を保存するリスト
client = CHaserConnect.Client() # サーバーと通信するためのインスタンス
client.init(name)

def main():
    values = client.searchLeft() # サーバーに行動内容を伝える

while True: # ここからループ
    values = client.getReady() # サーバーに行動準備が完了したと伝える
    if values[0] == 0:
        break

    main()

    if values[0] == 0:
        break
