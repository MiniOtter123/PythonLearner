print("   ", end='')
for i in range(1, 10):
    print(f'{i:4}', end='')
print()

for i in range(1, 10):
    print(f'{i:<3}', end='')
    for j in range(1, 10):
        product = i * j
        print(f'{product:4}', end='')
    print()
