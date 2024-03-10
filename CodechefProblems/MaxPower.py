n = int(input())
a = input()
a = a[::-1]
for i in range(n):
    if a[i] == "1":
        print(i)
        break