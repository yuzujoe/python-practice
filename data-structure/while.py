count = 0

while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

while count < 5:
    print(count)
    count += 1
else:
    print('done')
