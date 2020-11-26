class Clock:
    # 1시 30분 48초인 시계 인스턴스 생성
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    # 13초를 늘린다, 그리고 변환한다.
    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
        elif self.minute >= 60:
            self.minute = 0
            self.hour += 1
        elif self.hour >= 24:
            self.hour = 0

    # 시계의 현재 시간 출력
    def __str__(self):
        self.second = str(self.second).zfill(2)
        self.minute = str(self.minute).zfill(2)
        self.hour = str(self.hour).zfill(2)
        return "{}:{}:{}".format(self.hour, self.minute, self.second)

    # 2시 3분 58초로 시계 세팅
    def set(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)

# 13초를 늘린다
for i in range(13):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 23시 59분 57초로 세팅
clock.set(23, 59, 57)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)