jirst=int(input())
second=int(input())
third=int(input())

if jirst==second and jirst==third:
    print(3)
elif jirst==second or jirst==third or second==third:
    print(2)
else:
    print(0)