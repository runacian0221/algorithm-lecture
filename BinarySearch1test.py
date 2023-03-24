import random
## 함수
def binSearch(ary, fData):
    global count
    pos = -1
    start = 0
    end = len(ary) -1 
    while (start <= end):
        count +=1
        mid = (start + end) // 2
        if (ary[mid] == fData):
            pos = mid
            break
        elif (ary[mid] > fData):
            end = mid - 1
        else:
            start = mid + 1
    return pos


## 전역
count = 0
dataAry = [random.randint(0, 1000000000000) for _ in range(10000000)]
findData = random.choice(dataAry)
dataAry.sort()

## 메인
print('배열-->', dataAry[0:20])
position = binSearch(dataAry, findData)
if (position == -1):
    print('검색 실패!')
else:
    print(findData, '가', position, '번째 있어요!-->', count, '번')