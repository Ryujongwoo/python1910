# 큰따옴표나 작은따옴표로 묶어주면 문자열 데이터로 취급한다.
memo = 'Hello\nWorld'
print(memo)
print('*' * 50)
memo = 'Python\nis\nGOOD!'
print(memo)
print('*' * 50)

# 큰따옴표 안에 작은따옴표를 넣을 수 있고 작은따옴표 안에 큰따옴표를 넣을 수 있다.
print('제2외국어를 배운 호랑이가 "야옹" 했습니다.')
print("제2외국어를 배운 호랑이가 '야옹' 했습니다.")
# 큰따옴표 안에 큰따옴표를 넣으려면 \"를 사용하고 작은따옴표 안에 작은따옴표를 넣으려면 \'
# 를 사용한다.
print('제2외국어를 배운 호랑이가 \'야옹\' 했습니다.')
print("제2외국어를 배운 호랑이가 \"야옹\" 했습니다.")
print('*' * 50)

# 큰따옴표나 작은따옴표 3개를 사용하면 여러 줄 문자열을 표시할 수 있다.
memo = """개울가에
올챙이 한마리
꼬물꼬물 헤엄치다"""
print(memo)
print('*' * 50)
memo = '''앞다리가 쏘옥
뒷다리가 쑤욱
팔딱팔딱 메뚜기됬네'''
print(memo)
print('*' * 50)

# 문자열 인덱싱(1문자 꺼내기) 또는 슬라이싱(범위를 지정해서 여러 문자 꺼내기)
# 인덱싱은 문자열의 특정 위치의 1문자를 얻어오는 것을 의미하고 슬라이싱은 여러 문자를
# 잘라내는 것을 의미한다.
string = 'We are the champoins, My friend!'

# 인덱싱 => [인덱스]
print(string[0]) # W
print(string[11]) # c
print(string[-1]) # !
print('*' * 50)

# 슬라이싱 => [시작위치:끝위치]
# 문자열에서 시작위치 부터 끝위치 - 1 번째 문자열을 얻어온다.
print(string[3:6]) # are
print(string[11:20]) # champoins
# 슬라이싱을 할 때 시작위치를 생략하면 처음 부터를 의미하고 끝위치를 생략하면 마지막 까지를
# 의미한다.
print(string[:20]) # We are the champoins
print(string[22:]) # My friend!
print('*' * 50)

# 인덱싱을 이용해 문자열의 일부를 수정할 수 없다.
string = 'pithon'
print(string)
print(string[1])
# string[1] = 'y' # 에러 발생
print(string[:1]) # p
print(string[2:]) # thon
string = string[:1] + 'y' + string[2:]
print(string)











