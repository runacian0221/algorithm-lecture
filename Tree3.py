## 함수
import random
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None
nameAry = [random.randint(0,100000000) for _ in range(1000000)]
## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)
for name in nameAry[1:] : # [ '레드벨벳', '마마무', ...
    node = TreeNode()
    node.data = name
    current = root
    while True :
        if (name < current.data) :
            if (current.left == None) :
                current.left = node
                break
            current = current.left
        else :
            if (current.right == None) :
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진 탐색 트리 구성 완료!!')

## 구성 결과를 저장해서 사용하기..

## 저장된 결과를 불러와서 찾기.
findName = random.choice(nameAry)
current = root
count = 0
while True :
    count += 1
    if (findName == current.data) :
        print(findName, '찾음~~ 뮤비 스타트~')
        break
    elif (findName < current.data) :
        if (current.left == None) :
            print(findName, '없어요 ㅠ')
            break
        current = current.left
    else :
        if (current.right == None) :
            print(findName, '없어요. ㅠ')
            break
        current = current.right

print(count, '번만에 성공/실패함.')