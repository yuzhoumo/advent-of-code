with open('input.txt', 'r') as f:
    t = f.readlines()

for i in range(len(t)):
    t[i] = int(t[i])//3-2

print(sum(t))
