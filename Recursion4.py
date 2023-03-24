## 함수
def factValue(num):
    if (num == 1):
        return 1
    return num * factValue(num-1)


## 메인
print(factValue(10))