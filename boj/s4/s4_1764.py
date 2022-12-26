# 입력
n, m = map(int,input().split())
listen_list = []
watch_set = set()
for i in range(n):
    listen_list.append(input())

for i in range(m):
    watch_set.add(input())

# 계산1: 듣보잡 수 구하기
dict_person = {}
for listen in listen_list:

    if listen in watch_set:

        if listen in dict_person:
            dict_person[listen] += 1

        dict_person[listen] = 1

# 계산2: 정렬
sorted_person = sorted(dict_person.items())

# 출력
print(len(sorted_person))
for person in sorted_person:
    print(person[0])
