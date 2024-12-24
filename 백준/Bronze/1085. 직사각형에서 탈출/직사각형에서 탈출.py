x, y, w, h = map(int, input().split())

cnt_list = []

cnt_list.append(x)
cnt_list.append(y)
cnt_list.append(w-x)
cnt_list.append(h-y)

print(min(cnt_list))