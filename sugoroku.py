import random

masu = 30
saikoro = 6
rest = masu

print ('ゲームスタート')
while rest > 0:
    value = random.randint(1,saikoro)
    print ('サイコロの目：' + str(value))
    rest -= value
    if rest > 0:
        print ('残り' + str(rest) + 'マスです')

if rest <= 0:
    print ('ゴール！')
