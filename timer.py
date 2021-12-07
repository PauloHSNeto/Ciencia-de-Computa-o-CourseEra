import time
t = 1
for c in range(10, 0, -1):
    print(c)
    mins = t // 60
    secs = t % 60
    time.sleep(t)
    t = t +1
print("DALE!!!")
