import random as rnd
def ArrayChange():
    mas=[]
    chars=['a', 'b', 'c']
    newmas=[]
    for i in range(10):
        mas.append(rnd.sample(chars, rnd.randint(1, 5)))
    for i in range(10):
        if(len(mas[i])<=3):
            newmas.append(mas[i])
    print(mas)
    print(newmas)
if __name__ == '__main__':
    ArrayChange()
