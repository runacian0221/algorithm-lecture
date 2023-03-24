## 함수
def printStar(num):
    if (num > 0):
        printStar(num-1) 
        # num이 0보다 크면 printStar(num-1) 실행 아래 프린트문 출력X
        print('*' * num)


## 메인
printStar(5)