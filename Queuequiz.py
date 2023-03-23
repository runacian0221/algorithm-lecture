## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        print('큐가 꽉 차지 않음')
        return False
    if (rear == SIZE-1 and front == -1):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    # if (rear == SIZE -1):
    #     return True
    # else:
    #     return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐 꽉참')
        return
    rear += 1
    data = queue[rear]


def isQueueEmpty(data):
    global SIZE, queue, front, rear
    if (rear == front):
        return True
    else:
        return False

def deQueue(data):
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비어있음') # 추출할 데이터가 없음
        return
    front +=1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비어있음')
        return
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front=rear=-1

## 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('*이쪽으로~ ', retData)
retData = deQueue()
print('*이쪽으로~ ', retData)

print('출구<--', queue, '<--입구')

enQueue('재남')
print('출구<--', queue, '<--입구')

enQueue('지민')
print('출구<--', queue, '<--입구')

enQueue('홍길동')
print('출구<--', queue, '<--입구')