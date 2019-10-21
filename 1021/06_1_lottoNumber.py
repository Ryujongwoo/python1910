import random
import time

# 추첨기를 준비한다.
# 로또 추첨기로 사용할 빈 리스트를 선언한다.
lotto = []

# 추첨기에 1 ~ 45의 공을 넣는다.
for i in range(1, 46):
    # print(i)
    lotto.append(i)
# ============================================
# print(lotto)

# 섞는다.
# lotto[0]와 lotto[1] ~ lotto[44] 사이의 값 중에서 랜덤한 위치에 있는 값과
# 교환한다.
for i in range(0, 1000000):
    # randrange(a, b) : a와 b-1 사이의 값 중에서 무작위수를 얻어온다.
    # print(random.randrange(1, 45))
    r = random.randrange(1, 45)
    lotto[0], lotto[r] = lotto[r], lotto[0]
# ============================================
# print(lotto)

# 1등 번호를 출력한다.
print('1등 번호 : ', end = '')
for i in range(0, 6):
    print('{0:02d} '.format(lotto[i]), end = '')
    # sleep() : 인수로 지정된 시간 만큼 프로그램을 잠깐 멈춘다.
    # 시간은 초 단위로 지정한다.
    time.sleep(1)
# ============================================
print('뽀나스 : {0:02d}'.format(lotto[6]))











