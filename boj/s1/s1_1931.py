# 입력
n = int(input())
time_arr = []
for _ in range(n):
    a,b = map(int,input().split())
    time_arr.append((a,b))

# 계산1: 정렬 (끝,시작)
time_arr.sort(key=lambda x: (x[1], x[0]))

# 계산2: 시작과 end의 -1 비교
end = [0]
cnt = 0

for time in time_arr:
    if time[0] >= end[-1]:
        end.append(time[1])
        cnt += 1
print(cnt)