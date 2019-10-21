import random as ran
import time as t

# 미국 로또는 1 ~ 69 사이에서 5개, 1 ~ 26 사이에서 1개

powerball = []

for i in range(1, 70):
    powerball.append(i)

for i in range(0, 1000000):
    r = ran.randrange(1, 69)
    powerball[0], powerball[r] = powerball[r], powerball[0]

print('흰공 : ', end = '')
for i in range(0, 5):
    print('{0:02d} '.format(powerball[i]), end = '')
    t.sleep(1)
print('빨강공 : {0:02d}'.format(ran.randrange(1, 27)))
