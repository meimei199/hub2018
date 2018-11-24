import random
class Computer:
    def play(self):
        num = random.randint(1,3)
        return num
class Person:
    def play(self):
        num = int(input('用户请出拳（ 石头 （1）/ 剪刀 (2)  / 布  (3）'))
        return num
def main():
    p1 = Person()
    p2 = Computer()
    p1_opt = p1.play()
    p2_opt = p2.play()
    print('p1出了%d '% p1_opt)
    print('p2出了%d '%p2_opt)
    if p1_opt == p2_opt:
        print('平局')
    elif ((p1_opt == 1 and p2_opt == 2)
          or (p1_opt == 2 and p2_opt == 3)
          or (p1_opt == 3 and p2_opt == 1)):
        print('p1赢')
    else:
        print('p2赢')
if __name__ == '__main__':
    main()



