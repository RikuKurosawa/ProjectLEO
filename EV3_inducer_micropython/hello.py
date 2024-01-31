#!/usr/bin/env micropython

'''Hello to the world from ev3dev.org'''

import os
import sys
import time
import socket
from sys import modules, stdin
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from ev3dev2.button import Button

#from pyb import I2C
import pyb
from pyb import I2C

i2c = I2C(6)






ip = "192.168.0.100"
po = 7700
mode = 0
flag = 0


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

def inq(str):
    global ltr
    print("inq")
    ltr = str
    client = Client()







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

def inq(bytes):
    global ltr
    print("inq")
    ltr = bytes
    client = Client()

def firstmove():

    global mode
    global ip
    global po
    bu = Button()

    ip = "192.168.0.100"
    po = 7700



    print("Hi, I'm pc3! I'll help your job")
    print("Please select the mode")
    print("to online mode, press the left button")
    print("to offline mode, press the right button")

    while True:#起動時、設定をユーザーに問う
        #モード選択

        if bu.left:
            mode = 1
            print("mode:online")
            break

        if bu.right:
            mode = 2
            print("mode:offline")
            break



    if mode == 1:#online

        print("set the IP", ip)
        print("\n")

        print("set the port", po)
        print("\n")



        inq(b"here_pc3")

        print("done first move")

def pcready():
    global MSG
    global flag

    if flag == 1:
        return

    inq(b"pc3_ready")

    if MSG != b"go":

        while True:

            if MSG == b"go":
                break
            if MSG == b"end":
                flag = 1
                break
            inq(b"waiting pc3"  )


    if flag ==1:
        inq(b"pc3_end")
    else:
        inq(b"pc3_start_job")

    if flag == 1:#いらないけどなんとなく
        return

def last():

    global ltr
    global MSG
    global mode
    global flag

    if flag == 1:
        return


    inq(b"pc3_done")

    if MSG != b"last":


        while True:
            inq(b"waiting last pc3")
            if MSG == b"last":
                break

    inq(b"pc3_last")

def finalmove():

    global MSG
    global flag


    if flag == 1:
        return

    inq(b"final_mode")

    if MSG == b"continue":#この中身に、隣の部屋へ
        import doing
        doing.main()


def main():
    global mode

    sound = Sound()
    sound.set_volume(100)
    print(b"welcome to EV3!")
    sound.speak(b'Welcome to Ev3!')

    firstmove()

    if mode == 1:

        while True:
            pcready()

            import config

            if config.x == 1:
                import ini
                ini.main()

            last()

            finalmove()
    else:
        while True:
            if TouchSensor().wait_for_bump(10,10):
                import doing
                doing.main()




    """
    '''The main function of our program'''

    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Hello World!')

    # print something to the output panel in VS Code
    debug_print('Hello VS Code!')


    # wait a bit so you have time to look at the display before the program
    # exits
    time.sleep(5)
    """


"""
# state constants
ON = True
OFF = False


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)

"""

main()
