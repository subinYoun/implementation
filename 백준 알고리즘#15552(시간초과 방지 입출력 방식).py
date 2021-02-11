import sys #sys.stdin.readline을 사용해야 할 때 넣어줌
n=int(input())

for _ in range(n):
    a, b=map(int, sys.stdin.readline().split()) #for문을 돌 경우 시간초과가 발생할 수 있으므로 입출력방식을
    # input()에서 sys.stdin.readline을 사용해야 할 때가 있음
    print(a+b)