k=0
pol=""
flag=True
iskoodid=[]
arvud=[]

while 1:
    k+=1
    print(k)
    ik=""
    while len(ik)!=11:
        try:
            ik=input("Введи личный код: ")
        except:
            ValueError
    ik1=int(ik[0])
    if 1<=ik1<=6:
        if ik1%2==0:
            pol="Женский"
        else:
            pol="Мужской"
        ik23=int(ik[1]+ik[2])#год
        ik45=int(ik[3]+ik[4])#месяц #50402080017
        ik67=int(ik[5]+ik[6])#день
        isik=int(str(ik[7])+str(ik[8])+str(ik[9]))
        if 0<=ik23<=99 and 1<=ik45<=12 and 1<=ik67<=31:
            data=str(ik67).zfill(2)+"."+str(ik45).zfill(2)+"."+str(ik23).zfill(2)#11.10.76
            kontrol=int(ik[-1])
            n=1
            summa=0
            #5040208001    ,7
            ikk=str(int(ik)//10)
            for i in ikk: #1*5+2*0+3*4
                if n==10: n=1
                summa+=int(i)*n
                n+=1
            kontroll=summa-(summa//11)*11 #kontrol==kontroll?
            if kontrol==kontroll:
                print("Личный код верный")
                iskoodid.append(ik)
            else:
                print("Личный код не верный, контрольный номер не ок")
                arvud.append(ik)

            if 1<=isik<=10:
                reg="Kuressaare Haigla"
            elif 11<=isik<=19:
                reg="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
            elif 21<=isik<=220:
                reg="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
            elif 221<=isik<=270:
                reg="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
            elif 271<=isik<=370:
                reg="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
            elif 371<=isik<=420:
                reg="Narva Haigla"
            elif 421<=isik<=470:
                reg="Pärnu Haigla"
            elif 471<=isik<=490:
                reg="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
            elif 491<=isik<=520:
                reg="Järvamaa Haigla (Paide)"
            elif 521<=isik<=570:
                reg="Rakvere, Tapa haigla"
            elif 571<=isik<=600:
                reg="Valga Haigla"
            elif 601<=isik<=650:
                reg="Viljandi Haigla"
            elif 651<=isik<=700:
                reg="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
            print(pol, data)
            print(reg)
    else:
        arvud.append(ik)
    if k==5: break