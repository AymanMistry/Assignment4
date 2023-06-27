# for with else loop
for i in "ayman":
    if i=="m":
        break
    else:
        print(i)
else:
    print("This has break")

for i in "ayman":
    if i=="n":
        pass
    else:
        print(i)
else:
    print("This has pass")


for i in "ayman":
    if i=="y":
        continue
    else:
        print(i)
else:
    print("This has continue")

#while with else loop
i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)
else:
    print("This has break")

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)
else:
    print("This has continue")

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)
else:
    print("This has pass")