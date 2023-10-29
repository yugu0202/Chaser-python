import socket
import ipaddress
import os

class Client:
    def __init__(self, name, host=None, port=None):
        self.host = host if host is not None else input("接続先IPアドレスを入力してください\n>")
        self.port = port if port is not None else input("接続先ポート番号を入力してください\n>")
        self.name = name
        if self.host == "localhost":
            self.host = "127.0.0.1"

        if not self.__ip_judge(self.host):
            os._exit(1)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((self.host, int(self.port)))
        except:
            print(self.name + "はサーバに接続出来ませんでした")
            print("サーバが起動しているかどうか or ポート番号、IPアドレスを確認してください")
            os._exit(0)
        else:
            print(self.name + "はサーバに接続しました")

        print("port:", self.port)
        print("name:", self.name)
        print("host:", self.host)

        self.__str_send(self.name + "\r\n")

    def __ip_judge(self, host):
        try:
            ipaddress.ip_address(host)
        except Exception as e:
            print("IPアドレスの形式に誤りがあります : {0}".format(e))
            return False
        else:
            return True

    def __str_send(self, send_str):
        try:
            self.client.sendall(send_str.encode("utf-8"))
        except:
            print("send error:{0}\0".format(send_str))

    def __order(self, order_str, gr_flag = False):
        if gr_flag:
            responce = self.client.recv(4096)

            if(b'@' in responce):
                pass # Connection completed.
            else:
                print("Connection failed.")

        self.__str_send(order_str + "\r\n")

        responce = self.client.recv(4096)[0:11].decode("utf-8")

        if not gr_flag:
            self.__str_send("#\r\n")

        result = [int(x) for x in responce[0:10]]
        if result is None:
            result = [0 for i in range(10)]
        return result


    def getReady(self):
        try:
            print(self.name + "はgetReadyをサーバに送信")
            return self.__order("gr", True)
        except:
            print(self.name + "はgetReadyをサーバに送信できませんでした")

    def walkRight(self):
        print(self.name + "はwalkRightをサーバに送信")
        return self.__order("wr")

    def walkUp(self):
        print(self.name + "はwalkUpをサーバに送信")
        return self.__order("wu")

    def walkLeft(self):
        print(self.name + "はwalkLeftをサーバに送信")
        return self.__order("wl")

    def walkDown(self):
        print(self.name + "はwalkDownをサーバに送信")
        return self.__order("wd")

    def lookRight(self):
        print(self.name + "はlookRightをサーバに送信")
        return self.__order("lr")

    def lookUp(self):
        print(self.name + "はlookUpをサーバに送信")
        return self.__order("lu")

    def lookLeft(self):
        print(self.name + "はlookLeftをサーバに送信")
        return self.__order("ll")

    def lookDown(self):
        print(self.name + "はlookDownをサーバに送信")
        return self.__order("ld")

    def searchRight(self):
        print(self.name + "はsearchRightをサーバに送信")
        return self.__order("sr")

    def searchUp(self):
        print(self.name + "はsearchUpをサーバに送信")
        return self.__order("su")

    def searchLeft(self):
        print(self.name + "はsearchLeftをサーバに送信")
        return self.__order("sl")

    def searchDown(self):
        print(self.name + "はsearchDownをサーバに送信")
        return self.__order("sd")

    def putRight(self):
        print(self.name + "はputRightをサーバに送信")
        return self.__order("pr")

    def putUp(self):
        print(self.name + "はputUpをサーバに送信")
        return self.__order("pu")

    def putLeft(self):
        print(self.name + "はputLeftをサーバに送信")
        return self.__order("pl")

    def putDown(self):
        print(self.name + "はputDownをサーバに送信")
        return self.__order("pd")
