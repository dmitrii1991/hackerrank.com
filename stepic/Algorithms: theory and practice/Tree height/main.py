n = int(input())
data = list(map(int, input().split()))

save_data = [None] * n

def get_height(p):
    if save_data[p] is not None:
        return save_data[p]
    if p == -1:
        return 1
    h = 1 + get_height(data[p])
    save_data[p] = h
    return h


rezult = 0

for p in data:
    h = get_height(p)
    rezult = max(h, rezult)

print(rezult)
