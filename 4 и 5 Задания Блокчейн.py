#Задание 4
a = 483
c = 780
d = 622

#Задание 5
one = "a0d177b4967a6d99f4ff117defe1c0d23d4e78ca4630febcb948ee9e4520eff3"     # в "..." вставляем hash, который уже дан по заданию
two = 549     # пишим число, которое дано по заданию




# Ничего не тронгай ниже
import hashlib
x = 1
b = 1
print("Задание 4:")
o = str(hashlib.sha256(str(a).encode()).hexdigest())
print("1:",o)
h = o + str(hashlib.sha256(str(c).encode()).hexdigest())
o = str(hashlib.sha256(str(h).encode()).hexdigest())
print("2:",o)
j = o + str(hashlib.sha256(str(d).encode()).hexdigest())
o = str(hashlib.sha256(str(j).encode()).hexdigest())
print("3:",o)
two1 = hashlib.sha256(str(two).encode()).hexdigest()
string = one + two1
while x != 1001:
    s = hashlib.sha256(str(b).encode()).hexdigest()
    gg = string
    gg += s
    gg = hashlib.sha256(str(gg).encode()).hexdigest()
    if gg[:2] == "00":
        i = gg
    x += 1
    b += 1
print()
print("Задание 5:")
print("Пишешь в ответ:", i)
