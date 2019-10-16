string = 'We are the champoins, My friend!'

# len() : 인수로 지정된 문자열을 구성하는 문자의 개수를 얻어온다.
print(string)
print(len(string)) # 32
print(string[-1]) # !
print(string[len(string) - 1]) # !
print('*' * 50)

# count() : 인수로 지정된 문자열의 출연 횟수를 얻어온다.
print(string.count('e')) # 4
print(string.count('we')) # 0
print(string.count('We')) # 1
print('*' * 50)

# find() : 인수로 지정된 문자열이 처음 나타나는 위치를 얻어온다.
print(string.find('the')) # 7
print(string.find('The')) # -1, 찾는 문자열이 없으면 -1을 리턴한다.
print('*' * 50)

# index() : 인수로 지정된 문자열이 처음 나타나는 위치를 얻어온다.
print(string.index('the')) # 7
# print(string.index('The')) # 에러, 찾는 문자열이 없으면 에러가 발생된다.
print('*' * 50)

string = 'TjoeunIT'

# join() : 인수로 지정된 문자열에 '.'앞의 문자열을 삽입한다.
print('/'.join(string)) # T/j/o/e/u/n/I/T
print('^^;'.join(string)) # T^^;j^^;o^^;e^^;u^^;n^^;I^^;T
print('*' * 50)

# upper() : 문자열을 무조건 대문자로 변환한다.
# lower() : 문자열을 무조건 소문자로 변환한다.
print(string.upper()) # TJOEUNIT
print(string.lower()) # tjoeunit
print('*' * 50)

string = '   python   '

print(string)
print(len(string)) # 12
# lstrip() : 문자열 왼쪽의 불필요한 공백을 제거한다.
print(string.lstrip())
print(len(string.lstrip())) # 9
# rstrip() : 문자열 오른쪽의 불필요한 공백을 제거한다.
print(string.rstrip())
print(len(string.rstrip())) # 9
# strip() : 문자열 양쪽의 불필요한 공백을 제거한다.
print(string.strip())
print(len(string.strip())) # 9
print('*' * 50)

string = 'My are the champoins, My friend!'

# replace(old, new) : old 문자열을 new 문자열로 치환한다.
print(string.replace('My', 'Your'))
print('*' * 50)

# split() : 문자열을 구분자를 경계로 나눈다. => 나눈 결과는 list 타입으로 변환된다.
print(string.split()) # ['My', 'are', 'the', 'champoins,', 'My', 'friend!']
print(type(string.split())) # <class 'list'>
print('*' * 50)

# strip()의 재발견
# strip()은 문자열 양쪽의 불필요한 공백을 제거하는 목적으로 주로 사용되지만
print('   python   '.strip())
# 꼭 공백만 제거하는 것은 아니다.
print('www.example.com')
print('www.example.com'.strip('w')) # .example.com
print('www.example.com'.strip('w.com')) # example
print('*' * 50)

# replace()의 재발견
# 모든 공백 제거
print(' Hello   world '.strip()) # Hello   world
print(' Hello   world '.replace(' ', '')) # Helloworld

# join()과 split()을 이용해서 공백문자 2개 이상인 경우에 공백문자를 1개만 나오게 한다.
print(' '.join(' Hello         world '.split())) # Hello world
print(' Hello         world '.split()) # ['Hello', 'world']


