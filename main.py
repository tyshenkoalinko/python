import random as rnd
def ArrayChange():
    mas=[]
    chars=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p']
    newmas=[]
    for i in range(10):
        k=rnd.randint(1, 5)
        s=""
        for j in range(k):
            s+=rnd.sample(chars, k)[j]
            mas.append(s)
    for i in range(10):
        if(len(mas[i])<=3):
            newmas.append(mas[i])
    print(mas)
    print(newmas)
if __name__ == '__main__':
    ArrayChange()
