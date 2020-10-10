# No idea!

n_m = input()
aux = n_m.split(" ")
n = int(aux[0])
m = int(aux[1])

n_input = input()
n = n_input.split(" ")

a_input = input()
a = set(a_input.split(" "))

b_input = input()
b = set(b_input.split(" "))

happiness = 0
for i in n:
    if a.__contains__(i):
        happiness += 1
    if b.__contains__(i):
        happiness -= 1

print(happiness)
