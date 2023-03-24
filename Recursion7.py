## 함수
def gugu(dan, num):
    print('{0} * {1} = {2}'.format(dan, num, dan*num))
    if num < 9:
        gugu(dan, num+1)


## 메인
for dan in range(2, 10):
    print(f'## {dan}단 ##')
    gugu(dan, 1)