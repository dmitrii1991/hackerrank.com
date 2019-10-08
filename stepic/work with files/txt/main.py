file = open('input.txt', encoding='utf-8')
file2 = open('input1.txt', 'w', encoding='utf-8')
human = file.read()
data = human.split()
far = {}
for i in data:
    b = far.setdefault(i, 0)
    far[i] += 1
MyList = list(far)
i = 0
for w in far:
    i += 1
    MyList[i - 1] = (far[w], w)
for j in range(max(far.values()), 0, -1):
    for k in sorted(x for x in far if far[x] == j):
        print(k, file=file2, end=' ')
