# tuple 만들기  
# tuple은 list와 거의 비슷하지만 list는 []로 둘러싸고 tuple은 ()로 둘러싼다는 것과 list는 값을 수정, 삭제가 가능하지만 tuple은 불가능하다는 점이 다르다.

t1 = () # 빈 튜플 만들기
print(t1)
# 1개의 데이터만 가지는 튜플을 만들어야 하는 경우 반드시 ','를 찍어야 한다.
t2 = (1,)
print(t2)
t3 = (1, 2)
print(t3)
t4 = (1, 2, 3)
print(t4)
# 튜플은 ()를 생략해도 변수 하나에 ','로 구분해서 여러개의 데이터를 넣으면 튜플이 된다.
t5 = 1, 2, 3, 4 # () 생략
print(t5)
t6 = ('a', 'b', ('ab', 'cd'))
print(t6)
t7 = tuple() # 생성자를 사용해 빈 튜플을 만들 수 있다.
print(t7)
print(t6[0])
# t6[0] = 'z' # 튜플의 값을 수정하려 했으므로 에러가 발생된다.
# del t6[0] # 튜플의 값을 삭제하려 했으므로 에러가 발생된다.

# # 리스트와 같이 인덱싱과 슬라이싱이 가능하다.

# 인덱싱
print(t6[0])
print(t6[2])
print(t6[2][1])
# 슬라이싱
print(t6[0:2])
print(t6[:2])
print(t6[1:])
# 덧셈
print(t5 + t6)
# 곱셈
print(t5 * 3)
# 튜플에 저장된 데이터의 개수
print(len(t6))


