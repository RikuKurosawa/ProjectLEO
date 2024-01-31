

# cofing: utf-8

import socket
import time
from sys import stdin


ip = "192.168.0.100"
po = 7700
naoip = "192.168.0.103"

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
    global mode
    global cm
    global flag
    global ip
    global po
    global naoip

    print("Hi, I'm pc3! I'll help your job!\n")
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
        print("Please input the NAO IP")
        am = stdin.readline()
        am = am.strip()

        if am.strip() == "standard":

            break

  
        a = am
        print("OK?[y/n]",a)
        aa = stdin.readline()
        if aa.strip() == "y":
            naoip = am
            break

    print("set the  NAO IP", naoip)
    print("\n")

    while True:
        print("please set client START mode[auto/manual]")

        am = stdin.readline()
        a = am.strip()

        if a== "manual":
            cm = "manual"
            break

        if a== "auto":
            cm = "auto"
            break

    while True:
        print("please set client LAST mode[auto/manual]")

        am = stdin.readline()
        a = am.strip()

        if a== "manual":
            mode = "normal"
            break

        if a== "auto":
            mode = "full"
            break




    ltr =b"here_pc3"
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

    if cm == "manual":
        while True:        
            print("ready?[y]")
            am = stdin.readline()
            if am.strip() == "y":
                break
    ltr = b"pc3_ready"
    inq()

    if MSG != "go":

        ltr = "waiting pc3"  
        while True:
            
            if MSG == "go":
                break
            if MSG == "end":
                flag = 1
                break
            inq()
                

                

        
    if flag ==1:
        ltr = "pc3_end"
    else:
        ltr = "pc3_start_job"
    inq()

    if flag == 1:#いらないけどなんとなく
        return


def last():

    global ltr
    global MSG
    global mode
    global cm
    global flag

    if flag == 1:
        return

    if mode !="full":
        print("when you fiinsh process please input [f]")
    
        while True:
            am = stdin.readline()
            if am.strip() == "f":
                break

    ltr = b"pc3_done"
    inq()

    if MSG != "last":

        ltr = "waiting last pc3"  
        while True:
            inq()
            if MSG == "last":
                break

    ltr = "pc3_last"
    inq()    

def main():

    global ltr
    global MSG
    global mode
    global cm
    global flag

    if flag == 1:
        return

    print("ああマントルが饒舌に火を吹き上げて")
    time.sleep(1)

def finalmove():

    global ltr
    global MSG
    global mode
    global cm
    global flag

    
    if flag == 1:
        return

    ltr = "final_mode"
    inq()
    
    if MSG == "continue":#この中身に、隣の部屋へ

        print("move to next room")

    else:
        
        print("Thank you for coming!")


#これより下、プログラム動作


firstmove()

while True:

    pcready()

    main()

    last()
    
    finalmove()

    if flag == 1:
        break









