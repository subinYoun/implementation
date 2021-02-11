#맵의 크기
n, m = map(int, input().split())
#방문위치 저장
d=[[0]*m for _ in range(n)]
#캐릭터 위치, 방향
x, y, direction=map(int, input().split())
d[x][y]=1

array=[]
#맵 정보(육지0, 바다1)
for i in range(n):
    array.append(list(map(int, input().split())))
#북동남서 이동을 위한
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
#왼쪽으로 회전함수
def turn_left():
    global direction
    direction -= 1
    if direction==-1:
        direction=3
turn_time=0
count=1
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    if array[nx][ny]==0 and d[nx][ny]==0:
        x=nx
        y=ny
        d[nx][ny]=1
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny]==1:
            break
        else:
            x=nx
            y=ny
        turn_time=0
print(count)