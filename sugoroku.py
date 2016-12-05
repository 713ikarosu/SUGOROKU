import random

masu = 0
saikoro = 6
rest = masu


print ('ゲームスタート')
def main():
    global rest
    while rest > 0:
        SaikoroSystem()
        RestInput()
        Goal()

def masuDecision():
    global masu
    global rest
    masu = int(input('マス数を入力してください(20~39)：'))
    rest = masu
    while masu < 20 or masu > 39:
        masu = int(input('範囲内で入力してください(20~39)：'))
        rest = masu

def Goal():
    global rest
    if rest == 0:
        print ('ゴール！')
    elif rest < 0:
        rest *= -1
        print ('残り'+ str(rest) + 'マスです')

def SaikoroSystem():
    global rest
    value = random.randint(1,saikoro)
    print ('サイコロの目：' + str(value))
    rest -= value


def RestInput():
    if rest > 0:
        print ('残り' + str(rest) + 'マスです')


masuDecision()
main()
