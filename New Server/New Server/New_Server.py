
# cofing: utf-8

from sys import stdin
import socket



#mode Variation manual,auto


ltr = "John"
pc1 = "pc1"
pc2 = "pc2"
pc3 = "pc3"
pc4 = "normal"#ロボ校（あとから来たヒト用）
pc5 = "pc5"# LEGO
job = "yet"
bon = 0
count = 0
am = "something"
res = 0
f = 0

po = 7700

ip = "192.168.0.100"


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Server:

    global ip
    global po
    #サーバの定義（呼び出されて最初にやること）
    def __init__(self):
        self.ip = ip#サーバーIPアドレスの設定
        self.port = po#ポート番号の設定
        self.socket_make(self.ip, self.port)#ポート作り


    def socket_make(self,ip,port):
        #ソケット作り等々
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ソケット作り 
        self.s.bind((ip,port))#サーバー起動
        self.s.listen(10)#接続待ち

        while True:
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
            if pc1 == "end" and pc2 == "end" and pc3 == "end" and pc4=="end" and pc5 =="end":
                break



def Pr(str1):
    global pc1
    global pc2
    global pc3
    global pc4
    global pc5
    global bon
    global count
    global res
    global mode
    global job

    ans = "please wait"
    cs = "y"

    print("pc1=>",pc1)
    print("pc2=>",pc2)
    print("pc3=>",pc3)
    print("pc4=>",pc4)
    print("pc5=>",pc5)

    print("reserve",res)
    print("count",count)
    
    if bon == 0:

        if pc1 == "ready" and pc2 == "ready" and pc3 == "ready" and pc5 == "ready":
            if mode == "manual" or count <= 0:
                if mode != "fullauto":
                        print "Start?[y/n]"
                        cs = stdin.readline()
                        cs = cs.strip()                       

            if cs == "y":
                bon = 1
                ans = "go"
                count = count + 1
        if count > res or cs != "y" :#入力された回数と、実行した回数の比較
            print("the end")
            bon = 2
            ans = "end"

        if pc1 == "done" and pc2 == "done" and pc3 == "done":
                print("the done")
                bon = 3
                ans = "last"
                job = "done"
       

    if bon == 3:#すべてのマシンがlastするまで繰り返しlastを促す
        if pc4 == "normal" and pc1 == "last" and pc2 == "last" and pc3 == "last":
                bon = 0
        else:
            ans = "last"
   
    if bon == 1:#すべてのマシンがrunするまで繰り返しrunを促す
        if pc1 == "run" and pc2 == "run" and pc3 == "run":
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

    if str1 == "pc5_ready":
        pc5 = "ready"

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

    if str1 == "here_pc1":#クライアントが初期の際に、初期化
         ans = "welcome!_pc1"
         pc1 = "pc1"
    if str1 == "here_pc2":
         ans = "welcome!_pc2"
         pc2 = "pc2"
    if str1 == "here_pc3":
         ans = "welcome!_pc3"
         pc3 = "pc3"
    if str1 == "here_pc4":
         ans = "welcome!_pc4"
         pc4 = "normal"
    if str1 == "here_pc5":
        ans  = "welcome!_pc5"
        pc5 = "pc5"

    if str1 == "pc1_end":
         ans = "see you"
         pc1 = "end"
    if str1 == "pc2_end":
         ans = "see you"
         pc2 = "end"
    if str1 == "pc3_end":
         ans = "see you"
         pc3 = "end"
    if str1 == "pc4_end":
        ans = "see you"
        pc4 = "end"
    if str1 == "pc5_end":
        ans = "see you"
        pc5 = "end"

    if str1 == "pc4_want_to_start":
        if pc1 =="run"or pc2 == "run" or pc3 =="run":
            pc4 = "will run"
            ans = "ok_pc4"
    if str1 == "pc4_start":
        pc4 ="run"
        ans = "good luck pc4!"

    if str1 == "pc4_finish":
        pc4 = "normal"
        ans = "good work pc4"

    if str1 == "what's mode?":
        if mode == 3 or mode == 4:
            ans = "full"

        else:
            ans = "normal"

    if str1 == "final_mode":
        if count  % 2 == 0:
            ans = "end"
        else:
            ans = "continue"

    if str1 == "waiting pc5":#pc5への指示
        if count % 2 ==1:
            if job == "done":
               job = "yet"
               ans = "go_pc5"
    
    if str1 == "pc5_start_job":
        pc5 = "run"
        ans = "good_luck_pc5"

    if str1 == "pc5_done":
        pc5 == "pc5"
        ans = "good_work_pc5"

    return ans



print("Hello! I'm server !I'll help your briefing session! ")

print("\n")


while True:#起動時、設定をユーザーに問う
    print("set the host IP")
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

#起動時の設定
print("please select action mode.")
print("auto or manual?.....or fullauto?")



while True:#起動時、設定をユーザーに問う

    am = stdin.readline()
    
    if am.strip() == "auto" or "fullauto":
        
         if am.strip() == "auto":
            print("selected auto")       
            mode ="auto"
            break
         if am.strip() == "fullauto":
            ("selected fullauto")  
            mode = "fullauto"
            break


         if am.strip() == "manual":
            print("selected manual")
            mode = "manual"
            res = 9999
        
            break

         else :
            print("please input auto or manual or fullauto")       
        
if mode != "manual":
    while True:
        print("How many times do you want to run it?")
        an = stdin.readline()
        am = an.strip()          
        if is_int(am):
            am = int(am)
            if am % 2 == 0:

                print(am,"times")

                res = int(am) #超重要！！！！！！！(int と strは比較できないらしい)      
                f = 1
                break
            else:
                print("It's not even. continue?[y/n]")
                while True:
                    cs = stdin.readline()
                    cs = cs.strip()  
                    if cs =="y":
                        f =1
                        break
                    if cs == "n":
                        break
            if f == 1:
                break
        else:
            print("please input number")

f =0



server = Server()#サーバーの実行
