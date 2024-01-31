

# cofing: utf-8

import socket
import time
from sys import stdin


ip = "192.168.0.100"
po = 7700
legoip = "192.168.0.107"

ltr = b"Riku"
MSG = "MA"
mode = "normal"
cm = "hito"
flag = 0

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Client:
    #クライアントの定義（呼び出されて最初にやること）
    def __init__(self):
        self.server_ip = ip
        self.server_port = 7700
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

def firstmove():

    global ltr
    global MSG
    global legog
    global legos
    global flag
    global ip
    global po
    global legoip

    print("Hi, I'm pc5! I'll help your job!\n")
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
        print("Please input the LEGO IP")
        am = stdin.readline()
        am = am.strip()

        if am.strip() == "standard":

            break

  
        a = am
        print("OK?[y/n]",a)
        aa = stdin.readline()
        if aa.strip() == "y":
            legoip = am
            break

    print("set the  LEGO IP", legoip)
    print("\n")

    while True:
        print("please set LEGO START mode[auto/manual]")

        am = stdin.readline()
        a = am.strip()

        if a== "manual":
            legos = "manual"
            break

        if a== "auto":
           legos = "auto"
           break   

    while True:
        print("please set LEGO GOAL mode[auto/manual]")

        am = stdin.readline()
        a = am.strip()

        if a== "manual":
            legog = "normal"
            break

        if a== "auto":
            legog = "full"
            break




    ltr =b"here_pc5"
    inq()

    print("done first move")

def pcready():
    global ltr
    global MSG
    global mode
    global cm
    global flag

    if flag == 1:
        return


    ltr = b"pc5_ready"
    inq()

    if MSG != "go_pc5":

        ltr = "waiting pc5"  
        while True:
            
            if MSG == "go_pc5":
                break
            if MSG == "end":
                flag = 1
                break
            inq()
                

                

        
    if flag ==1:
        ltr = "pc1_end"
    else:
        ltr = "pc5_start_job"
    inq()

    if flag == 1:#いらないけどなんとなく
        return


def main():

    global ltr
    global MSG
    global legos
    global legog
    global flag

    if flag == 1:
        return
    if legos == "manual":
        print("lego first part レゴレゴ")#ここで、レゴのスイッチのオンオフ(while文)
    else:
        time.sleep(10)#自動スタートなので、移動を待つ秒数
    print("捨てられた野に立つ人を")
    #移動

    if legog == "manual":
        print ("lego final part　テトテト")#ここで、レゴのスイッチのオンオフ(while文)
        time.sleep(10)#客が座るまでここで稼ぐ
    

def finalmove():

    global ltr
    global MSG
    global mode
    global cm
    global flag

    
    if flag == 1:
        return

    ltr = "pc5_done"
    inq()
    



#これより下、プログラム動作


firstmove()

while True:

    pcready()

    main()
    
    finalmove()

    if flag == 1:
        break
    lnt = "pc5_end"
    inq()








