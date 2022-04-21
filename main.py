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
    print('4 - печать БД')
    n=int(input())
    if n == 4:
        for i in range(len(r)):
            d1=r[i].vremya[0]
            d2=r[i].vremya[1]
            if str(d2)=='0':
                print(r[i].punkt,r[i].pometka,str(d1) + ':'+ str(d2)+'0')
            else:
                print(r[i].punkt, r[i].pometka, str(d1) + ':' + str(d2))

print("-")


