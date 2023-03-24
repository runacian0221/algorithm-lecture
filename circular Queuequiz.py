## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ((rear+1) % 5 == front):
        return True
    else:
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('원형큐가 꽉참')
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
    
def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        return
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        return
    data = queue[(front+1) % SIZE]

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


# retData = deQueue()
# print('*이쪽으로~ ', retData)
# print('## 다음 대기 손님 :', peek())
# retData = deQueue()
# print('*이쪽으로~ ', retData)
# retData = deQueue()
# print('*이쪽으로~ ', retData)
# print('출구<--', queue, '<--입구')