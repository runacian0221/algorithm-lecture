import random
## 함수
def selectionSort(ary):
    n = len(ary)    # 데이터 개수
    for i in range(0, n-1):
        minIdx = i
        for j in range(i+1, n):
            if (ary[minIdx] > ary[j]):
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary

## 전역
dataAry = [random.randint(30, 200) for _ in range(8)]


## 메인
print('정렬 전-->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후-->', dataAry)