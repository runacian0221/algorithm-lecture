## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE-1 and front == -1): # 모든 큐가 꽉찬경우
        return True
    elif (rear == SIZE-1 and front != -1):
        # 한칸씩만 땡기기
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1  # 한칸씩 땡겨주기
        rear -= 1   # 한칸씩 땡겨주기
        return False
    # else:
    #     (rear == SIZE-1 and front != -1):
    #     # 한칸씩만 땡기기
    #     for i in range(front+1, SIZE):
    #         queue[i-1] = queue[i]
    #         queue[i] = None
    #   front -= 1  # 한칸씩 땡겨주기
    # rear -= 1   # 한칸씩 땡겨주기
    # return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
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


# retData = deQueue()
# print('*이쪽으로~ ', retData)
# print('## 다음 대기 손님 :', peek())
# retData = deQueue()
# print('*이쪽으로~ ', retData)
# retData = deQueue()
# print('*이쪽으로~ ', retData)
# print('출구<--', queue, '<--입구')