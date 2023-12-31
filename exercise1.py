n = input()
m = list(set(map(int,input().split())))
print(sorted(m)[round(len(m)/2)])