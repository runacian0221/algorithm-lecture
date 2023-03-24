## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx



## 전역
dataAry = [55, 88, 33, 77]


## 메인
minPos = findMinIndex(dataAry)
print('최솟값-->', dataAry[minPos])