if True:
    print("True")
else:
    print("False")

if 1 in [1,2,3]:
    print("1 있음")
elif 3:
    print("3 있음")
else :
    print("없음")
 
score = 50
message = "success" if score >= 60 else "failure"
print(message)

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

for i in range(1,5):
    print("i는 %s입니다." %i)