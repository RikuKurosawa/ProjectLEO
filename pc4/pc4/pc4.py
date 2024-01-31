

# cofing: utf-8

import socket
import time
import sys
from sys import stdin

ltr = b"Riku"
MSG = "MA"
mode = "Susumu"
ip = "192.168.0.100"
po =7700
nao3ip = "192.168.0.105"
nao4ip = "192.168.0.106"

f =0

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Client:
    global ip
    #クライアントの定義（呼び出されて最初にやること）
    def __init__(self):
        self.server_ip = ip
        self.server_port = po
        self.socket_make(self.server_ip, self.server_port)


    def socket_make(self,ip,port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ソケット作り 
        self.s.connect((ip, port))
        self.s.send(ltr)
        print("sent:",ltr)
        time.sleep(1)#出力調整
        data = self.s.recv(1024)
        global MSG
        MSG = data
        print("received:",data)
def inq():
   client = Client()

def check_last():
    ltr = "Human-Le"
    inq()
    if MSG == "last":
        ltr = "pc4_finish"

    return "True"   

def first ():
    global ltr
    global mode
    global nao3ip
    global nao4ip
    global ip
    global po



    print("Hi, I'm pc4! I'll help your job!\n")
    while True:#起動時、設定をユーザーに問う
        print("Please input the host IP")
        am = stdin.readline()
        am = am.strip()

        if am.strip() == "standard":

            break

  
        a = am
        print("OK?[y/n]",a)
        aa = stdin.readline()
        if aa.strip() == "y":
            ip = am
            break

    print("set the IP", ip)
    print("\n")


    while True:#起動時、設定をユーザーに問う
        print("set the port")
        am = stdin.readline()
        am = am.strip()

        if am.strip() == "standard":

            break

  
        if is_int(am):

            print("OK?[y/n]",am)
            aa = stdin.readline()
    
            if aa.strip() == "y":
                po = int(am)
                break

        else:
            print("please input the number")

    print("set the port", po)
    print("\n")
   
    while True:#起動時、設定をユーザーに問う
        print("Please input the NAO-3 IP")
        am = stdin.readline()
        am = am.strip()

        if am.strip() == "standard":

            break

  
        a = am
        print("OK?[y/n]",a)
        aa = stdin.readline()
        if aa.strip() == "y":
            nao3ip = am
            break

    print("set the  NAO-3 IP", nao3ip)
    print("\n")   

    while True:#起動時、設定をユーザーに問う
        print("Please input the NAO-4 IP")
        am = stdin.readline()
        am = am.strip()

        if am.strip() == "standard":

            break

  
        a = am
        print("OK?[y/n]",a)
        aa = stdin.readline()
        if aa.strip() == "y":
            nao4ip = am
            break

    print("set the  NAO-4 IP", nao4ip)
    print("\n")
    
    ltr = "here_pc4"
    inq()



def main():#メインコンテンツ

    #if check_last():←この2つで更新をチェック
        #return

#ここに内容


    print("main")


#以下、本プログラム
first()

while True:
    while True:#ここでstartを図る
            print("Please input [start] to start the Program")
            am = stdin.readline()
            if am.strip() == "start":
                ltr ="pc4_want_to_start"
                while True:
                    inq()
                    if MSG =="ok_pc4":
                        f = 1
                        break
                    if MSG == "end":
                        ltr = "pc4_end"
                        inq()
                        f=2
                        break
            if f == 1:
                f=0
                break
            if f == 2:
                break

    if f == 2:
        break
    ltr ="pc4_start"
    inq()

    main()


    while True:#無言で、サーバーのラスト待ち
        ltr = "pc4_wait_last"
        inq()
        if MSG == "last":
            ltr = "pc4_finish"
            print("もう終わっちゃいます")
            break

    #ここより下に、案内等




    #以下、プログラム終了通知をサーバへ
    ltr = "pc4_finish"
    inq()