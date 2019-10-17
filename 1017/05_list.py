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
print('*' * 50)

# 리스트 슬라이싱
d = [10, 20, 30, 40, 50]
print(d[0:2]) # [10, 20]
print(d[:3]) # [10, 20, 30]
print(d[2:]) # [30, 40, 50]
print('*' * 50)

e = [1, 2, 3, ['a', 'b', 'c'], 4]
print(e[2:4]) # [3, ['a', 'b', 'c']]
print(e[3][:2]) # ['a', 'b']
print('*' * 50)

# 리스트에서 인덱싱으로 뽑아내면 상수가 리턴되고 슬라이싱으로 뽑아내면 리스트가
# 리턴된다.
print(e[0]) # 1
print(type(e[0])) # <class 'int'>
print(e[0:1]) # [1]
print(type(e[0:1])) # <class 'list'>
print('*' * 50)

# 리스트 연산자
# '+'는 두 개의 리스트를 연결하고 '*'는 리스트를 반복한다.
f = [1, 2, 3]
g = [4, 5, 6, 7]
print(f + g) # [1, 2, 3, 4, 5, 6, 7]
print(f * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print('*' * 50)

# 리스트의 수정 및 삭제
a = [1, 2, 3]
print(a) # [1, 2, 3]
a[1] = 4 # 수정
print(a) # [1, 4, 3]
print('*' * 50)
a[1:2] = ['a', 'b', 'c']
print(a) # [1, 'a', 'b', 'c', 3]
a[2] = ['d', 'e', 'f']
print(a) # [1, 'a', ['d', 'e', 'f'], 'c', 3]

a[2:3] = [] # 슬라이싱 방식은 빈 리스트를 넣어주면 삭제된다.
print(a) # [1, 'a', 'c', 3]
del a[2] # 인덱싱 방식은 del 명령으로 삭제한다.
print(a) # [1, 'a', 3]
print('*' * 50)

# ============================================================================

# 리스트 메소드

# append(data) : 리스트의 맨 뒤에 데이터를 추가한다.
a = [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]
print('*' * 50)

# insert(index, data) : 리스트의 index 번째 위치에 데이터를 삽입한다.
a.insert(1, 5)
print(a) # [1, 5, 2, 3, 4]
# insert()와 len()으로 append() 구현하기
# a.insert(-1, 6)
# print(a) # [1, 5, 2, 3, 6, 4]
a.insert(len(a), 6)
print(a) # [1, 5, 2, 3, 4, 6]
print('*' * 50)

# sort() : 리스트에 저장된 데이터를 오름차순으로 정렬한다.
a.sort()
print(a) # [1, 2, 3, 4, 5, 6]
b = ['c', 'a', 'd', 'b']
b.sort()
print(b) # ['a', 'b', 'c', 'd']
c = ['홍길동', '임꺽정', '장길산', '일지매']
c.sort()
print(c) # ['일지매', '임꺽정', '장길산', '홍길동']
print('*' * 50)
# sort() 메소드의 괄호 안에 reverse = True 옵션을 지정하면 내림차순으로 정렬된다.
a.sort(reverse = True)
print(a) # [6, 5, 4, 3, 2, 1]
print('*' * 50)

# reverse() : 리스트에 저장된 데이터를 뒤집는다.
a = [4, 1, 3, 2]
a.reverse()
print(a) # [2, 3, 1, 4]
a.sort()
print(a) # [1, 2, 3, 4]
a.reverse()
print(a) # [4, 3, 2, 1]
print('*' * 50)

# index() : 리스트에 저장된 데이터가 있을 경우 첫 번째 데이터의 위치를 얻어온다.
# 실행 결과가 0 이상이면 리스트에 데이터가 포함되어 있다.
a = [1, 2, 3, 4, 3, 5, 3]
print(a.index(3)) # 2
# print(a.index(6)) # 데이가 리스트에 없을 경우 에러가 발생된다.
print('*' * 50)

# count() : 리스트에 저장된 특정 데이터의 개수를 얻어온다.
# 실행 결과가 1 이상이면 리스트에 데이터가 포함되어 있다.
print(a.count(3)) # 3
print(a.count(6)) # 0
print('*' * 50)

# remove() : 리스트의 데이터를 제거한다. => 첫 번째 데이터만 제거한다.
b = a.remove(3)
print(b) # None
print(a) # [1, 2, 4, 3, 5, 3]
print('*' * 50)

# pop() : 리스트에 저장된 데이터를 얻어온 후 삭제한다.
b = a.pop()
# pop() 메소드에서 데이터의 위치를 지정하지 않으면 마지막 데이터를 의미한다.
print(b) # 3
print(a) # [1, 2, 4, 3, 5]
b = a.pop(1)
# pop() 메소드에서 데이터의 위치를 지정하면 지정된 위치의 데이터를 의미한다.
print(b) # 2
print(a) # [1, 4, 3, 5]
print('*' * 50)

# extend() : 리스트를 확장한다. 즉, 리스트에 리스트를 더한다.
a = [1, 2, 3]
a.extend([4, 5])
print(a) # [1, 2, 3, 4, 5]
b = [1, 2, 3]
b = b + [4, 5]
print(b) # [1, 2, 3, 4, 5]
c = [1, 2, 3]
c += [4, 5]
print(c) # [1, 2, 3, 4, 5]

# 연산자 우선순위
# () => 단항연산자 => 이항연산자 => 삼항연산자 => 대입연산자
# 이항 연산자의 우선순위
# **(거듭제곱) => *, /, //, % => +, - => 관계연산자(>, >=, <, <=, ==, !=)
# => 논리연산자(and, or)











