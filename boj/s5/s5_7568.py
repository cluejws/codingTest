# 입력
import sys
input = sys.stdin.readline

n = int(input())
people = []
for _ in range(n):
    person = list(map(int,input().split()))
    people.append(person)
    
# 그냥 모두 비교해보면서 등수 더하기
# ㅅㅂ...
for i in range(len(people)):
    cnt = 1
    for j in range(len(people)):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                cnt += 1
    print(cnt, end=" ")

            
                
