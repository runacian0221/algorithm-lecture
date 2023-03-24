## 함수
class Graph():
    def __init__(self, size):
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

## 전역
SIZE = 4
G1 = None
A, B, C, D = 0, 1, 2, 3

## 메인
G1 = Graph(SIZE)
G1.graph[A][B] = 1; G1.graph[A][C] = 1; G1.graph[A][D] = 1
G1.graph[B][A] = 1; G1.graph[B][C] = 1
G1.graph[C][A] = 1; G1.graph[C][B] = 1; G1.graph[C][D] = 1
G1.graph[D][A] = 1; G1.graph[D][C] = 1


for row in range(SIZE):
    for col in range(SIZE):
        print(G1.graph[row][col], end = ' ')
    print()
print()