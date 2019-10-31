def selectionSortAsc(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data

def selectionSortDesc(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data

# if __name__ == '__main__'를 사용하는 이유
# if __name__ == '__main__'를 사용한 프로그램을 실행할 때는 별 차이를 모른다.
# 현재 파일이 다른 파일에 모듈로 포함된 경우 if __name__ == '__main__'를 사용하지 않으면
# 모듈이 삽입된 파일에서 현재 파일에서 실행한 프로그램이 실행된다.
# if __name__ == '__main__'를 사용하면 현재 파일이 다른 모듈에 삽입된 경우
# if __name__ == '__main__'에 코딩한 프로그램은 실행되지 않는다.
if __name__ == '__main__':
    print('selectionSortModule.py 파일에서 실행되는 프로그램')
    data = [8, 3, 4, 9, 1]
    data = selectionSortAsc(data)
    print('오름차순 정렬 결과 : {}'.format(data))
    data = selectionSortDesc(data)
    print('내림차순 정렬 결과 : {}'.format(data))

