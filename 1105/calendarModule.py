# 달력 제작에 필요한 함수를 만든다.

# 년도를 인수로 넘겨받아 윤년/평년을 판단해 윤년이면 True, 평년이면 False를 리턴하는 함수
# 논리값을 기억하는 변수나 논리값을 리턴하는 함수의 이름은 'is'로 시작하는 것이 관행이다.
def isLeapYear(year):
    # 년도가 4로 나눠 떨어지고 100으로 나눠 떨어지지 않거나 400으로 나눠 떨어지면 윤년이다.
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# 년, 월을 인수로 넘겨받아 그 달의 마지막 날짜를 리턴하는 함수
def lastDay(year, month):
    # 12달의 마지막 날짜를 기억하는 리스트를 만든다.
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 윤년/평년에 따른 2월의 마지막 날짜를 결정한다.
    m[1] = 29 if isLeapYear(year) else 28
    # 그 달의 마지막 날짜를 리턴시킨다.
    return m[month - 1]

# 년, 월, 일을 인수로 넘겨받아 1년 1월 1일 부터 지난 날짜의 합계를 리턴하는 함수
def totalDay(year, month, day):
    # 1년 1월 1일 부터 전년도 12월 31일 까지 지난 날짜를 계산한다.
    total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    # 전년도 까지 지난 날짜에 전달 까지 지난 날짜를 더한다.
    for i in range(1, month):
        total += lastDay(year, i)
    # 전달 까지 지난 날짜에 일을 더해 리턴시킨다.
    return total + day

# 년, 월, 일을 인수로 넘겨받아 요일을 숫자로 계산해서 리턴하는 함수
# 나머지가 0이면 일요일, 1이면 화요일, ..., 6이면 토요일
def weekDay(year, month, day):
    return totalDay(year, month, day) % 7

if __name__ == '__main__':
    print(isLeapYear(2019))
    print('윤년' if isLeapYear(2019) else '평년')
    print(lastDay(2019, 2))
    print(totalDay(2019, 11, 5))
    print(weekDay(2019, 11, 9))

