import random
## 함수
def seqSearch(ary, fData):
    pos = -1
    size = len(ary)
    for i in range(size):
        if (ary[i] == fData):
            pos = i
            break

    return pos


## 전역
dataAry = [random.randint(30, 200) for _ in range(8)]
findData = random.choice(dataAry)
#findData = 999


## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if (position == -1):
    print('검색 실패!')
else:
    print(findData, '가', position, '번째 있어요!')