'''对于所有评测用例，1 ≤ n ≤ 100，1 ≤ t ≤ 100，2 ≤ L ≤ 1000，0 < ai < L。L为偶数。
输入的第一行包含三个整数n, L, t，用空格分隔，分别表示小球的个数、线段长度和你需要计算t秒之后小球的位置。
第二行包含n个整数a1, a2, …, an，用空格分隔，表示初始时刻n个小球的位置。'''


class Ball():
    def __init__(self, pos, direc):
        self.p = pos
        self.d = direc


# read data
n, L, t = tuple(map(lambda x: int(x), input().split()))
poss = list(map(lambda x: int(x), input().split()))

# design data structure

balls = []
for p in poss:
    balls.append(Ball(p, 1))

for time in range(t):
    coord = {}
    for i in range(n):
        balls[i].p += balls[i].d
        if balls[i].p == L or balls[i].p == 0:
            balls[i].d *= -1
            continue

        if coord.get(balls[i].p) is None:
            coord[balls[i].p] = i
        else:
            balls[coord[balls[i].p]].d *= -1
            balls[i].d *= -1

for b in balls:
    print(b.p, end=' ')
