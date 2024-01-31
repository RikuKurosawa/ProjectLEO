

# cofing: utf-8

from sys import stdin
import socket



#mode 0 => none
#mode 1 => auto
#mode 2 => manual
#mode 3 => fullauto


ltr = "John"
pc1 = "pc1"
pc2 = "pc2"
pc3 = "pc3"
pc4 = "normal"#ロボ校（あとから来たヒト用）
bon = 0
count = 0
am = "something"
res = 0


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Server:
    #サーバの定義（呼び出されて最初にやること）
    def __init__(self):
        self.ip = "192.168.1.15"#サーバーIPアドレスの設定
        self.port = 7700#ポート番号の設定
        self.socket_make(self.ip, self.port)#ポート作り


    def socket_make(self,ip,port):
        #ソケット作り等々
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ソケット作り 
        self.s.bind((ip,port))#サーバー起動
        self.s.listen(3)#接続待ち

        while True:
            if bon ==2:
                break
            print("Waiting connection...")
            conn, addr = self.s.accept()#接続許可
            print("Connected by {}".format(addr))#どこから接続されているかを表示
            data = conn.recv(1024)#データの確認
            if not data:
                    break#データがなければ終了
            print("received",data)
            ltr = Pr(data)#問い合わせの内容を関数に入れ、答えを受け取る
            conn.send(ltr)
            print("sent",ltr)



def Pr(str1):
    global pc1
    global pc2
    global pc3
    global pc4
    global bon
    global count
    global res
    global mode

    ans = "please wait"
    cs = "hira"
    
    if bon == 0:

        if mode == 1 or mode == 3: #auto
            cs = "y"#聞かないときにもプログラムが回る
            if pc1 == "ready" and pc2 == "ready": # and pc3 == "ready":
                if count == 0:#初回のみスタートをユーザーに
                    print "Start?[y/n]"
                    cs = stdin.readline()
                    cs = cs.strip()                      

                if cs == "y":
                    bon = 1
                    ans = "go"
                    count+=1
                    if count > res:#入力された回数と、実行した回数の比較
                        bon = 2
                        ans = "end"

            if pc1 == "done" and pc2 == "done":# and pc3 == "done":
                    print("all computers has done")
                    bon3 = 3
                    ans = "last"

       
        if mode == 2: #manual
            if pc1 == "ready" and pc2 == "ready":# and pc3 == "ready":
                print "Start?[y/n]"
                cd = stdin.readline()
                

                if cd.strip() == "y":
                    bon = 1
                    ans = "go"
                else :
                    bon = 2
                    ans = "end"
        
            if pc1 == "done" and pc2 == "done":# and pc3 == "done":
                    print("all computers has done")
                    bon3 = 3
                    ans = "last"

    if bon == 3:#すべてのマシンがlastするまで繰り返しrunを促す
        if pc4 == "normal" and pc1 == "last" and pc2 == "last":# and pc3 == "last":
            bon = 0

        else:
            ans = "last"

    if bon == 1:#すべてのマシンがrunするまで繰り返しrunを促す
        if pc1 == "run" and pc2 == "run":# and pc3 == "run":
            bon = 0
        
        else:
            ans = "go"

    if bon == 2:#end後に問い合わせてきたマシンに、endを返す
        ans = "end"



    if str1 == "pc1_ready":#それぞれのready確認
        pc1 = "ready"
    
    if str1 == "pc2_ready":
        pc2 = "ready"

    if str1==  "pc3_ready":
        pc3 = "ready"

    if str1 == "pc1_done":#それぞれのdone確認
        pc1 = "done"
    
    if str1 == "pc2_done":
        pc2 = "done"

    if str1==  "pc3_done":
        pc3 = "done"

    


    if str1 == "pc1_start_job":#それぞれのマシンの仕事開始の確認
        pc1 = "run"
        ans = "good luck pc1"


    if str1 == "pc2_start_job":
        pc2 = "run"
        ans = "good luck pc2"

    if str1 == "pc3_start_job":
        pc3 = "run"
        ans = "good luck pc3"

    if str1 == "pc1_last":#それぞれのマシンの仕事終わりの確認
        pc1 = "last"
        ans = "good work pc1"


    if str1 == "pc2_last":
        pc2 = "last"
        ans = "good work pc2"

    if str1 == "pc3_last":
        pc3 = "last"
        ans = "good work pc3"

    if str1 == "here":
        if mode == 3:
            ans = "full"
        else:
            ans = "welcome!"

    if str1 == "pc4_start":
        pc4 = "run"
        ans = "手間隙かけて作ろう"

    if str1 == "pc4_finish":
        pc4 = "normal"
        ans = "仲良くしよう"

    return ans


'''

#print("Hello! I'll help your briefing session! ")#起動時の設定
#print("please select action mode.")
#print("auto or manual?.....or fullaout?")



while True:#起動時、設定をユーザーに問う

    am = stdin.readline()
    
    if am.strip() == "auto" or "fullauto":
        
         if am.strip() == "auto"("selected auto")       
            mode = 1      
         if am.strip() == "auto"("selected fullauto")  
            mode = 3
        print("How many times do you want to run it?")
        
        while True:
            
            am = stdin.readline()          
            tf = is_int(am)            
            if tf == True:
      
                print(am,"times")

                res = int(am)
           
                break
            
            else:
                print("please input number")


        break


    if am.strip() == "manual":
        print("selected manual")
        mode = 2
        
        break

    else :
        print("please input auto or manual")

'''
mode = 2
res = 3

server = Server()#サーバーの実行