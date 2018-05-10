age = int(input("请输入年龄:"))
if age >= 1 and age < 10:
    print("童年")
elif age >= 11 and age <= 20:
    print("少年")
elif age >= 21 and age <= 30:
    print("青年")
elif age >= 31 and age <= 40:
    print("壮年")
elif age >= 41 and age <= 60:
    print("中年")
elif age >= 61 and age <= 80:
    print("老年")
else:
    print("....")
