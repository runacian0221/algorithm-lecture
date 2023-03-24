import random
## 함수
def seqSearch2(ary, fData):
    pos = -1
    size = len(ary)
    for i in range(size):
        print('*비교:',ary[i])
        if (ary[i] == fData):
            pos = i
            break
        elif (ary[i] > fData):
            break
    return pos


## 전역
dataAry = [random.randint(30, 200) for _ in range(8)]
findData = random.choice(dataAry)
dataAry.sort()
findData = 99

## 메인
print('배열-->', dataAry)
position = seqSearch2(dataAry, findData)
if (position == -1):
    print('검색 실패!')
else:
    print(findData, '가', position, '번째 있어요!')