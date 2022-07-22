import socket
import ipaddress
import os

class Client:
    def init(self,name):
        self.host = input("接続先IPアドレスを入力してください\n>")
        self.port = input("接続先ポート番号を入力してください\n>")
        self.name = name
        if self.host == "localhost":
            self.host = "127.0.0.1"

        if not self.__ip_judge(self.host):
            os._exit(1)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((self.host, int(self.port)))
        except:
            print(self.name + "はサーバに接続出来ませんでした\nサーバが起動しているかどうか or ポート番号、IPアドレスを確認してください")
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
        print(responce)

        if not gr_flag:
            self.__str_send("#\r\n")

        return [int(x) for x in responce]


    def getReady(self):
        try:
            return self.__order("gr", True)
            print(self.name + "はgetReadyをサーバに送信")
        except:
            print(self.name + "はgetReadyをサーバに送信できませんでした")

    def walkRight(self):
        return self.__order("wr")
        print(self.name + "はwalkRightをサーバに送信")

    def walkUp(self):
        return self.__order("wu")
        print(self.name + "はwalkUpをサーバに送信")

    def walkLeft(self):
        return self.__order("wl")
        print(self.name + "はwalkLeftをサーバに送信")

    def walkDown(self):
        return self.__order("wd")
        print(self.name + "はwalkDownをサーバに送信")

    def lookRight(self):
        return self.__order("lr")
        print(self.name + "はlookRightをサーバに送信")

    def lookUp(self):
        return self.__order("lu")
        print(self.name + "はlookUpをサーバに送信")

    def lookLeft(self):
        return self.__order("ll")
        print(self.name + "はlookLeftをサーバに送信")

    def lookDown(self):
        return self.__order("ld")
        print(self.name + "はlookDownをサーバに送信")

    def searchRight(self):
        return self.__order("sr")
        print(self.name + "はsearchRightをサーバに送信")

    def searchUp(self):
        return self.__order("su")
        print(self.name + "はsearchUpをサーバに送信")

    def searchLeft(self):
        return self.__order("sl")
        print(self.name + "はsearchLeftをサーバに送信")

    def searchDown(self):
        return self.__order("sd")
        print(self.name + "はsearchDownをサーバに送信")

    def putRight(self):
        return self.__order("pr")
        print(self.name + "はputRightをサーバに送信")


    def putUp(self):
        return self.__order("pu")
        print(self.name + "はputUpをサーバに送信")

    def putLeft(self):
        return self.__order("pl")
        print(self.name + "はputLeftをサーバに送信")

    def putDown(self):
        return self.__order("pd")
        print(self.name + "はputDownをサーバに送信")
