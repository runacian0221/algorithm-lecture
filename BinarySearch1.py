import random
## 함수
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) -1
    while (start <= end):
        mid = (start + end) // 2
        if (ary[mid] == fData):
            pos = mid
            break
        elif(ary[mid] < fData):
            start = mid + 1
        else:
            end = mid - 1

    return pos


## 전역
dataAry = [random.randint(30, 200) for _ in range(8)]
findData = random.choice(dataAry)
dataAry.sort()

## 메인
print('배열-->', dataAry)
position = binSearch(dataAry, findData)
if (position == -1):
    print('검색 실패!')
else:
    print(findData, '가', position, '번째 있어요!')