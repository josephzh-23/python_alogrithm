
v = "123"
out = 0
for i in v:
    out = out * 10 + (ord(i) - ord("0"))
print(out)

out2 = 0
for i in v:
    if i.isdigit():
        out2 = out2 * 10 + int(i)

print("out 2 is", out2)
