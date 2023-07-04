def sum(a,b):
    result = a + b
    print("%d, %d의 합은 %d입니다." %(a,b,result))
    return result

def sum_many(*args): #여러개의 값
    sum = 0
    for i in args:
        sum += i
    return sum
print(sum_many(1,2,3,4,5))

def print_kwargs(**kwargs): #딕셔너리 여러개 받기
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 : " + kwargs[k])
print_kwargs(name="김동후", b="2")

def sum_and_mul(a,b): #리턴값은 하나만 나옴.(튜플))
    return a+b, a*b
print(sum_and_mul(1,2))

def say_myself(name, old, man=True): #매개변수 미리 설정하기.
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

add = lambda a, b: a+b #def add(a,b): return a+b

for i in range(10):
    print(i, end=" ")
print()

f = open("Practice/새파일.txt", 'w', encoding="UTF-8") #r읽기모드 w쓰기모드 a추가모드 파일생성
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("Practice/새파일.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break
    print(line, end="")
f.close()