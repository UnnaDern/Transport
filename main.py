import pickle
class Raspis:
    punkt = None
    pometka = None
    vremya = None


F1 = open('students.txt', 'r', encoding='utf-8')
r = []
while True:
    x = F1.readline()
    if not x: break
    x = x.split(' ', 3)
    rasp = Raspis()
    rasp.punkt = x[0]
    rasp.pometka = x[1]
    rasp.vremya = list(map(int, x[2].split(':')))
    r.append(rasp)

F1=open("students.dat","wb")
pickle.dump(r,F1)
F1.close()
F1=open("students.dat","rb")
A=pickle.load(F1)
while True:
    print('Введите необходимое число')
    print('1 - сортировка по станции назначения')
    print('2 - станция назначения,согласно времени отправления')
    print('3 - редактировование записи в БД')
    print('4 - печать БД')
    print('5 - выход из БД')
    n=int(input())
    if n == 4:
        for i in range(len(r)):
            d1=r[i].vremya[0]
            d2=r[i].vremya[1]
            if str(d2)=='0':
                print(r[i].punkt,r[i].pometka,str(d1) + ':'+ str(d2)+'0')
            else:
                print(r[i].punkt, r[i].pometka, str(d1) + ':' + str(d2))
    if n==1:
        r1=sorted(r,key=lambda x: x.punkt)
        for i in range(len(r)):
            d1=r1[i].vremya[0]
            d2=r1[i].vremya[1]
            if str(d2)=='0':
                print(r1[i].punkt,r1[i].pometka,str(d1) + ':'+ str(d2)+'0')
            else:
                print(r1[i].punkt, r1[i].pometka, str(d1) + ':' + str(d2))
    if n==2:
        print("Введите нужное вам время:")
        p=input().split(":")
        p1=p[0]
        p2=p[1]
        for i in range(len(r)):
            if r[i].vremya[0]==int(p1) and r[i].vremya[1]==int(p2):
                d1 = r[i].vremya[0]
                d2 = r[i].vremya[1]
                if str(d2) == '0':
                    print(r[i].punkt, r[i].pometka, str(d1) + ':' + str(d2) + '0')
                else:
                    print(r[i].punkt, r[i].pometka, str(d1) + ':' + str(d2))
            else:
                print("Такой электрички нет")
                print("--------***--------")
                break
    if n==3:
        print("Чтобы начать редактировать список введите 'Lets' или нажмите Enter")
        print("Чтобы закончить редактировать список введите 'Stop'")
        True
        while True:
            j = input('9')
            if j == 'Stop':
                break
            if j == 'Lets' or ' ':
                print("Введите строку")
                re = input()
                re = re.split(' ', 3)
                a = Raspis()
                a.punkt = re[0]
                a.pometka = re[1]
                a.vremya = list(map(int, re[2].split(':')))
                r.append(a)
    elif n==6:
        k=len(r)
        i=0
        p = input().split(":")
        p1 = p[0]
        p2 = p[1]
        while k!=0:
            for i in range(len(r)):
                if r[i].vremya[0] < int(p1):
                    print('0')
                    r.pop(i)
                    k-=1
                else:
                    i+=1
                    k-=1




