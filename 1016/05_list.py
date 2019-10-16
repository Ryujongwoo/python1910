# 리스트 만들기

# 리스트를 만들 때는 데이터를 []로 감싸주고 각각의 데이터는 ','로 구분한다.
odd = [1, 3, 5, 7, 9]
print(odd) # [1, 3, 5, 7, 9]
print(type(odd)) # <class 'list'>
print('*' * 50)

a = [] # 빈 리스트
print(a) # []
print(type(a)) # <class 'list'>
print('*' * 50)

# 빈 리스트는 생성자 함수를 이용해서도 만들 수 있다.
b = list()
print(b) # []
print(type(b)) # <class 'list'>
print('*' * 50)

c = [1, 2, 3] # 숫자 리스트
d = ['Life', 'is', 'too', 'short'] # 문자 리스트
e = [1, 2, 'Life', 'is'] # 숫자와 문자가 혼용된 리스트
f = [1, 2, ['Life', 'is']] # 리스트의 데이터 요소로 리스트를 가지는 리스트
g = [['Life', 'is'], ['too', 'short']] # 2행 2열인 2차원 리스트

# 리스트 인덱싱
a = [10, 20, 30, 40, 50]
print(a) # [10, 20, 30, 40, 50]
print(a[0]) # 10
print(a[0] + a[2]) # 40
print(a[-1]) # 50
print(len(a)) # 5
print('*' * 50)

b = [10, 20, 30, ['a', 'b', 'c']]
print(b) # [10, 20, 30, ['a', 'b', 'c']]
print(b[0]) # 10
print(b[3]) # ['a', 'b', 'c']
print(b[-1]) # ['a', 'b', 'c']
print(b[3][0]) # a
print('*' * 50)

c = [10, 20, ['a', 'b', ['Life', 'is']]]
print(c) # [10, 20, ['a', 'b', ['Life', 'is']]]
print(c[2]) # ['a', 'b', ['Life', 'is']]
print(c[2][2]) # ['Life', 'is']
print(c[2][2][1]) # is




